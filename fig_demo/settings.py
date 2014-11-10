"""
Django settings for fig_demo project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ht6=i#_kc#+v)6pgdv*5-tft2(@=q8s8c2_06-ueh(+^z#n^p+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_nose',
    'djcelery',
    'json_field',
    'rest_framework',
    'fig_demo.apps.account',
    'fig_demo.apps.page',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fig_demo.urls'

WSGI_APPLICATION = 'fig_demo.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
        'HOST': 'database'
    }
}

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}


# Celery config
# Broker
BROKER_TRANSPORT = 'redis'
BROKER_URL = 'redis://redis:6379/0'
BROKER_TRANSPORT_OPTIONS = {
    'fanout_prefix': True
}
# Queues
CELERY_DEFAULT_QUEUE = 'fig-emo'
# Results
CELERY_RESULT_BACKEND = BROKER_URL
# Events
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_SENT_EVENT = True
# Run under parent process
CELERY_ALWAYS_EAGER = bool(os.environ.get('CELERY_ALWAYS_EAGER', False))


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'


# Sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = 'default'


LOG_LEVEL = os.environ.get('LOG_LEVEL')

if LOG_LEVEL not in ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']:
    LOG_LEVEL = 'INFO'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '[%(asctime)s %(levelname)s] %(name)s:L%(lineno)d \'%(message)s\'',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'fig_demo': {
            'handlers': ['console'],
            'filters': [],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    }
}

# REST Framework
DATE_FORMAT_STRING = '%Y-%m-%dT%H:%M:%SZ'

# Testing
SOUTH_TESTS_MIGRATE = True
DDF_FILL_NULLABLE_FIELDS = False
