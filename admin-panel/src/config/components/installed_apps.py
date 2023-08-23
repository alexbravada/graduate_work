import os


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies.apps.MoviesConfig',
    'billing.apps.BillingConfig',
    'django_extensions',
    'corsheaders',
    'django_celery_results',
    'django_celery_beat',
]

debug = os.environ.get('DEBUG', False) == 'True'
if debug:
    INSTALLED_APPS.append('debug_toolbar')
