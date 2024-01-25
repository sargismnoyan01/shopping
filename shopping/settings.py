from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')


SECRET_KEY = 'django-insecure-9b0c&930s17jh+@5fdg9-$%=&zwv0qz%-0pkn!#qtt_2fhkn_x'

DEBUG = False

ALLOWED_HOSTS = ['*','16.171.146.195']



INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'jazzmin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    "phonenumber_field",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopping.urls'

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

WSGI_APPLICATION = 'shopping.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'armzona',
#         'USER':'postgres',
#         'PASSWORD':'727447Sa.',
#         'HOST':'192.168.0.104',
#         'PORT':'5432',

#     }
# }


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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='armenianzona@gmail.com'
EMAIL_HOST_PASSWORD='sfaqlgpmuhpcqymy'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'


STATIC_URL = '/static/'
MEDIA_ROOT = '/media/'

MEDIA_ROOT= os.path.join(BASE_DIR,'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'main', 'static_files')),



STATIC_ROOT = os.path.join(BASE_DIR, "static")


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AWS_ACCESS_KEY_ID = 'AKIAW3MECAM3WIIIHTGC'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'shopping0001'
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'shopping.backends.s3bot3.S3Boto3Storage'
