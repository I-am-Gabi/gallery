from gallery.settings.common import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASES_NAME'],  
        'USER': os.environ['DATABASES_USER'],
        'PASSWORD': os.environ['DATABASES_PASSWORD'],
        'HOST': os.environ['DATABASES_HOST'],
        'PORT': '',
        'CONN_MAX_AGE': 500,
    }
} 
 
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

