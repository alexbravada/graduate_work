# Проектная работа: диплом

Автор: [@alexbravada](https://github.com/alexbravada)
Ссылка на репозиторий (https://github.com/alexbravada/graduate_work/)

## Запуск проекта

1. Создаем файл .env на основе .env_example (копируем и редактируем)
2. Запускаем сборку и старт проекта:

```shell
docker-compose up --build  
```

3. Применяем миграции:

```shell
docker exec access-api alembic upgrade head
```

4. ОПЦИОНАЛЬНО: Создаем суперпользователя.

```shell
docker exec -it admin-panel bash
python3 manage.py createsuperuser
```

5. [Установить пакет Stripe в систему](https://stripe.com/docs/stripe-cli)
6. Запустить утилиту для перенаправления вебхуков stripe на локальный сервер (для разработки), указать в профиле stripe
   полученный ключ

```shell
stripe listen --forward-to 127.0.0.1:8000/api/v1/webhook/
```

Access API доступно
на http://127.0.0.1:8000/api/, [авто-документация](https://github.com/paQQuete/graduate_work/blob/dev/access-api/autodoc.json)

Admin Panel доступна на http://127.0.0.1:8000/admin/

## Краткое описание (подробности в презентации)

Для быстрого и общего понимания попробуем представить процесс добавления подписки и администратором, покупки этой
подписки клиентом и её отмены:

1. Администратор в админ панели создает Subscription, куда включает (помимо названия и описания) фильмы, которые входят
   в эту подписку, цену за день подписки и продолжительность подписки
2. По сигналу post_save данные о подписке доставляются в Stripe
3. Клиент может обратиться к **/api/v1/payment/card/{subscribe_id}** с нужным айди подписки, после чего его перенаправит
   на страницу с оплатой этой подписки
4. После оплаты подписки на вебхук приходит событие успешной оплаты, данные из него записываются в
   **billing.granted_access**, **billing.granted_films**, в которых есть поле available_until, оно позволяет в
   будущем с помощью периодических тасок Celery переводить is_active в False, по наступлении обозначенного времени
5. Фронтенд может обращаться к **/api/v1/subscribe/check/{movie_uuid}/{user_uuid}/** за получением подтверждения доступа
   к фильму
6. Рефанд осуществляется по id выданного гранта, **/api/v1/refund/grant/{grant_id}**, обсчитывается по фактически
   прошедшим дням после покупки подписки, причем день покупки - всегда считается за уже прошедший день

Важной особенностью проекта является система баланса, то есть каждая транзакция (top-up, spending, refund) находит
отражаение в **billing.transactions** и **billing.funds_hold**, с помощью чего можно обратиться к подробной истории
транзакций, пополнять пользовательский баланс без покупки фильма, иметь точное подтверждение того, можно ли на
конкретный запрос возврата средств возвращать их + меньше зависеть от Stripe. На время проведений чувствительных
операций (то есть возврата средств
пользователю) создаются временные транзакции-холды в отдельной таблице.

"Жирные" эндпоинты refund и webhook - следствие такой архитектуры

7. Пополнение баланса осуществляется по id юзера и сумме пополнения **/api/v1/topup/{user_id}/?amount={amount}**
8. Возврат средств с баланса происходит с привязкой к определенной транзакции, по её id *
   */api/v1/refund/transaction/{transaction_id}/**, при условии покрытия балансом этой транзакции (в операциях такого
   рода актуальный баланс всегда обсчитывается)

Также присутствует таблица **billing.trans_order**, в которую записываются ключи от Stripe, необходимые для правильного
возврата средств.

В Redis кэшируются данные checkout сессии Stripe, чтобы клиент при незавершенной оплате попадал в свою сессию.

Задачи по записи баланса в **billing.balance**, проверка и приостановка активной подписки по её истечению берёт на себя
Celery, интегрированная с Django (очередь сообщений RabbitMQ)
