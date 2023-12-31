import os
from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()
env_path = Path('') / '.env'
load_dotenv(dotenv_path=env_path)

include(
    'components/database.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/internationalization.py',
    'components/logging.py',
    'components/stripe.py',
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000', 'http://nginx']

INTERNAL_IPS = [
    '127.0.0.1',
    'nginx'
]

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']

#error 500 on open cascade menus (i.e. open the roletype menu on creation any filmwork) if this block on(and django toolbar is working)
def custom_show_toolbar(request):
    return True # Always show toolbar, for example purposes only.
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
}
##

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

