from pathlib import Path
from typing import Dict, List, Tuple, Union

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env: environ.Env = environ.Env(DEBUG=(bool, False))

DEFAULT_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS: List[str] = [
    "apps.core.apps.CoreConfig",
    "apps.auth.apps.AuthConfig",
    "apps.user.apps.UserConfig",
    "apps.invoice.apps.InvoiceConfig",
]

THIRD_PARTY_APPS: List[str] = [
    "django_extensions",
    "django_filters",
]

INSTALLED_APPS: List[str] = DEFAULT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK: Dict[str, Union[int, List[str], Tuple[str], str]] = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 15,
}


WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL: str = "apps_user.User"

BASE_API_PATH: str = "api"
APPEND_SLASH: bool = True

####################
#        AWS settings
# https://blog.devgenius.io/how-to-configure-a-django-application-with-s3-buckets-for-file-storage-9cea315316a4
#######################
USE_S3 = env.bool("USE_S3", False)

if USE_S3:
    AWS_ACCESS_KEY_ID = env.str("S3_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env.str("S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("S3_BUCKET_NAME")
    # AWS_S3_ENDPOINT_URL = env.str("S3_HOST")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_DEFAULT_ACL = "public-read"
    # AWS_LOCATION = 'static'

    # STATICFILES_DIRS = [
    #     'static',
    # ]
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # public media settings
    # PUBLIC_MEDIA_LOCATION = 'media'
    # MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    # DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"
