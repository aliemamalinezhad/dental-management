from .base import *


SECRET_KEY = 'v0c#!33+hz=@xk(3+hncg$&klh8u)nx$u+x@&xx@7r&c=nln^@'
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'dental_postgresql',
        'PORT': '5433',

    }
}
STATIC_URL = '/static/'











