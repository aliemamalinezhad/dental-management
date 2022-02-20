import dental_api.settings.base as base
import os

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(base.BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
