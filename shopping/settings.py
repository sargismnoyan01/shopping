from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')


SECRET_KEY = 'django-insecure-9b0c&930s17jh+@5fdg9-$%=&zwv0qz%-0pkn!#qtt_2fhkn_x'

DEBUG = False

ALLOWED_HOSTS = ['*','51.20.37.156']



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
STATIC_ROOT = os.path.join(BASE_DIR, "static_files")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'main', 'static'),
)

# Media files (user-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AWS_ACCESS_KEY_ID = 'AKIAW3MECAM36VBOJTGD'
# AWS_SECRET_ACCESS_KEY = 'MQkOjMZIEkI5mfhjiBnHGTeNSCzCoGNivdJmYHri'
# AWS_STORAGE_BUCKET_NAME = 'shopping0001'
# AWS_S3_REGION_NAME = 'eu-north-1'  # e.g., us-east-1

# # Static settings
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Media settings
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
