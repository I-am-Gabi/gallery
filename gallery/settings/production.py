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
        'NAME': 'gallery',
        'USER': 'gallery',
        'PASSWORD': 'gallery123',
        'HOST': 'localhost',
        'PORT': '',
    }
} 


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static')

db_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_env)