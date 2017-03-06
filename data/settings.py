import logging
import os
import sys

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG", False))


# As app is running behind a host-based router supplied by Heroku or other
# PaaS, we can open ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # misc 3rd party
    "django_extensions",
    "raven.contrib.django.raven_compat",

    # local apps
    "mi.apps.MiConfig",
    "wins.apps.WinsConfig",
    "users.apps.UsersConfig",

    # drf
    "rest_framework",
    "rest_framework.authtoken",
    "crispy_forms",

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'alice.middleware.SignatureRejectionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'data.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'data.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'


# User stuffs
AUTH_USER_MODEL = "users.User"
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/"


# Application authorisation
# used in signature middleware to determine if API request is signed by a
# server with shared secret, and if so which one.
UI_SECRET = os.getenv("UI_SECRET")
ADMIN_SECRET = os.getenv("ADMIN_SECRET")
MI_SECRET = os.getenv("MI_SECRET")
assert len(set([UI_SECRET, ADMIN_SECRET, MI_SECRET])) == 3,\
    "secrets must be different"


# DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "alice.authentication.NoCSRFSessionAuthentication",
    )
}


# Mail stuffs
FEEDBACK_ADDRESS = os.getenv("FEEDBACK_ADDRESS")
SENDING_ADDRESS = os.getenv("SENDING_ADDRESS")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = bool(os.getenv("EMAIL_USE_TLS"))
EMAIL_USE_SSL = bool(os.getenv("EMAIL_USE_SSL"))
EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT")) if os.getenv("EMAIL_TIMEOUT") else None
EMAIL_SSL_KEYFILE = os.getenv("EMAIL_SSL_KEYFILE")
EMAIL_SSL_CERTFILE = os.getenv("EMAIL_SSL_CERTFILE")
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")


# deleted wins from these users will not show up in deleted wins CSV
IGNORE_USERS = [
    'adam.malinowski@digital.bis.gov.uk',
    'daniel.quinn@digital.bis.gov.uk',
    'mateusz.lapsa-malawski@digital.bis.gov.uk',
    'paul.mccomb@ukti.gsi.gov.uk',
    'rob.sommerville@digital.bis.gov.uk',
    'christine.leaver@ukti.gsi.gov.uk',
    'gino.golluccio@ukti.gsi.gov.uk',
    'adrian.woodcock@digital.trade.gov.uk',
    'graham.veal@digital.trade.gov.uk',
    'sekhar.panja@digital.trade.gov.uk',
    'darren.mccormac@digital.trade.gov.uk',
    'emma.jackson@digital.trade.gov.uk',
]


# allow access to API in browser for dev
API_DEBUG = bool(os.getenv("API_DEBUG", False))


# Sentry
RAVEN_CONFIG = {
    "dsn": os.getenv("SENTRY_DSN"),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}


# Logging for development
if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
            },
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }

# only show critical log message when running tests
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    logging.disable(logging.CRITICAL)


# django countries only uses ISO countries. Wikipedia says, "XK is a
# 'user assigned' ISO 3166 code not designated by the standard, but used by
# the European Commission, Switzerland, the Deutsche Bundesbank..."
COUNTRIES_OVERRIDE = {
    'XK': 'Kosovo',
}
