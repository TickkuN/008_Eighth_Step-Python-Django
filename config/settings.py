from pathlib import Path
import environ  # postscript
from django.contrib import messages # postscript
import os
import dj_database_url
import django_heroku
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# postscript
env = environ.Env()
root = environ.Path(BASE_DIR / 'secrets')
 
# For production environment
# env.read_env(root('.env.prod'))
 
# For development environment
env.read_env(root('.env.dev'))
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')
 
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
 
 
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',  # postscript
    'storages'
]
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
 
ROOT_URLCONF = 'config.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # postscript
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.custom_context_processors.base',  # postscript
            ],
        },
    },
]
 
WSGI_APPLICATION = 'config.wsgi.application'
 
 
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)
 
 
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
 
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
 
LANGUAGE_CODE = 'en'
 
TIME_ZONE = 'Asia/Tokyo'  # changed
 
USE_I18N = True
 
USE_L10N = True
 
USE_TZ = True
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
# postscript
STATICFILES_DIRS = [
    BASE_DIR / 'static'
] 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# TAX_RATE
TAX_RATE = 0.1
 
# Stripe API Key
STRIPE_API_SECRET_KEY = env.str('STRIPE_API_SECRET_KEY')

# Schema & Domain
MY_URL = env.str('MY_URL')

# Custom User Model
AUTH_USER_MODEL = 'base.User'
 
LOGIN_URL = '/login/'
 
LOGIN_REDIRECT_URL = '/'
 
LOGOUT_URL = '/logout/'
 
LOGOUT_REDIRECT_URL = '/login/'
 
 
# messages
MESSAGE_TAGS = {
    messages.ERROR: 'rounded-0 alert alert-danger',
    messages.WARNING: 'rounded-0 alert alert-warning',
    messages.SUCCESS: 'rounded-0 alert alert-success',
    messages.INFO: 'rounded-0 alert alert-info',
    messages.DEBUG: 'rounded-0 alert alert-secondary',
}
 
# custom_context_processors
TITLE = 'TickkuN Market'

django_heroku.settings(locals())