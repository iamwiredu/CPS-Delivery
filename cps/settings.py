"""
Django settings for cps project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import json
from pathlib import Path
from urllib.parse import urlparse


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z^tj&whs9!3a=a+7^=7t^m7m!p2#yex-guem6#vud81-5lqj3c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", ".now.sh",'cpsdeliverygh.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'delivery',
    'crispy_forms',
    'crispy_bootstrap4',
    'adminConsole',
    'rider',
    'restaurant',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'

]

ROOT_URLCONF = 'cps.urls'

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

WSGI_APPLICATION = 'cps.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "verceldb",
#         'URL_NO_SSL':"postgres://default:dN0ShxHPfqa9@ep-misty-feather-a4wery4g-pooler.us-east-1.aws.neon.tech:5432/verceldb",
#         "URL":"postgres://default:dN0ShxHPfqa9@ep-misty-feather-a4wery4g-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require",
#         "PRISMA_URL":"postgres://default:dN0ShxHPfqa9@ep-misty-feather-a4wery4g-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require&pgbouncer=true&connect_timeout=15",
#         "URL_NON_POOLING":"postgres://default:dN0ShxHPfqa9@ep-misty-feather-a4wery4g.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require",
#         'USER': "default",
#         'PASSWORD':"dN0ShxHPfqa9",
#         "HOST":"ep-misty-feather-a4wery4g-pooler.us-east-1.aws.neon.tech"
#     }
# }
tmpPostgres = urlparse("postgresql://neondb_owner:npg_gbQ8DjAfp3KH@ep-misty-paper-a59qv5d9-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "neondb",
        'URL_NO_SSL': f"postgres://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}:5432/{tmpPostgres.path.replace('/', '')}",
        "URL": f"postgres://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}:5432/{tmpPostgres.path.replace('/', '')}?sslmode=require",
        "PRISMA_URL": f"postgres://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}:5432/{tmpPostgres.path.replace('/', '')}?sslmode=require&pgbouncer=true&connect_timeout=15",
        "URL_NON_POOLING": f"postgres://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}:5432/{tmpPostgres.path.replace('/', '')}?sslmode=require",
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        "HOST": tmpPostgres.hostname,
        'PORT': 5432,  # Default PostgreSQL port
    }
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# #Google Cloud Storage settings
# GS_PROJECT_ID = 'precise-line-437900-m9'
# GS_BUCKET_NAME = 'cps-images'

# # Get the JSON key data from environment variable
# google_cloud_key = os.getenv('KEY')

# # Parse the JSON key
# google_cloud_info = json.loads(google_cloud_key)

# # settings.py
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
#     google_cloud_info
# )

# # Media files (uploads)
# GS_MEDIA_BUCKET_NAME = GS_BUCKET_NAME
# MEDIA_URL = f'https://storage.googleapis.com/{GS_MEDIA_BUCKET_NAME}/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'productionFiles/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

