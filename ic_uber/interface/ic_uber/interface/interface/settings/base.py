"""
Django settings for interface project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import django_heroku


#============  INÍCIO #1 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========

#from decouple import config, Csv
from dj_database_url import parse as dburl 

#============  FIM #1 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

import psycopg2

# ======================
#import environ 

#env = environ.Env(
    # set casting, default value
    #DEBUG=(bool, False)
#)
# reading .env file
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6ox@8ecxy$w+&w0n*$jv2pa&ie&oli=f5%hb)9m$!9$ud7dz66'


#environ.Env.read_env()
#============  INÍCIO #2 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========

#SECRET_KET = env('SECRET_KEY')

#============  FIM #2 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#============ INÍICO #3 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========

#DEBUG= env('DEBUG', default= False, cast= bool)




#============ FIM #3 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========
ALLOWED_HOSTS = ['*',
'boiling-taiga-97630.herokuapp.com']


#============ INÍCIO # ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========
#ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=[])

#ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

#============ FIM #4 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========


# Application definition

INSTALLED_APPS = [
    'juris.apps.JurisConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_datepicker_plus',




#============ INÍCIO #5 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========
    'django_extensions',
    #'interface.juris',
#============ INÍCIO #5 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========
]

BOOTSTRAP4 = {
    'include_jquery': True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'interface.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'interface.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



#============ INÍCIO #6 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========
#default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
#DATABASES = {
    #'default': env('DATABASE_URL', default=default_dburl, cast=dburl),
#}
#============ INÍCIO #6 ADC COM TUTORIAL "Django e DataTables básico" - autor: RÉGIS DO PYHTON==========


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


LOGIN_REDIRECT_URL = '/juris/'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# I ADDED '"USE_THOUSAND_SEPARATOR' AFTER REGIS DO PYTHON'TUTORIAL 
USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/static/',
]

STATIC_ROOT= os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# ========STATIC FILES ============
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'static'),
#)


django_heroku.settings(locals())