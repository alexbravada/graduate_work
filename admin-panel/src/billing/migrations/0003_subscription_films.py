# Generated by Django 3.2 on 2023-05-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_filmwork_subscriptions'),
        ('billing', '0002_subscription_payment_gw_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='films',
            field=models.ManyToManyField(related_name='subscriptions_relations', through='billing.SubscriptionFilmwork', to='movies.Filmwork'),
        ),
    ]
