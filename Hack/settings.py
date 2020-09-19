import os
from .localsettings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "&vv91_0@)*uc$32+c^+6k0h$3r2#h4dzl_dr(bj%cux9q-7l6a"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "_h)na+xqf)2&w)91%$50$bv5m#^$4z*xo!sk!9cn7erfm99^o0"

DEBUG = True

ALLOWED_HOSTS = ["*","https://hackzurich2020.herokuapp.com/"]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


# Application definition

INSTALLED_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "USER",
    "cloudinary",
    "rest_framework",
    "drf_yasg",
    "tinymce",
    "django_filters",
    "oauth2_provider",
    "import_export",
    "django_rest_passwordreset",
    "taggit",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "Hack.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "template")],
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


WSGI_APPLICATION = "Hack.wsgi.application"

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DATETIME_FORMAT": "%Y-%m-%d",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, "images")

MEDIA_URL = "/media/"


STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

AUTH_USER_MODEL = "USER.User"


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

STATIC_DIRS = [os.path.join(BASE_DIR, "static")]

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

import dj_database_url

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(prod_db)

LOGOUT_URL = "/accounts/logout/"
LOGIN_REDIRECT_URL = "/swagger/"


ACCESS_TOKEN_EXPIRE_SECONDS = 12 * 60 * 60  # Token wil expire in 12 hours

OAUTH2_PROVIDER = {
    "SCOPES": {"read": "Read scope", "write": "Write scope",},
    "CLIENT_ID_GENERATOR_CLASS": "oauth2_provider.generators.ClientIdGenerator",
    "ACCESS_TOKEN_EXPIRE_SECONDS": ACCESS_TOKEN_EXPIRE_SECONDS,
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"



DJANGO_REST_PASSWORDRESET_IP_ADDRESS_HEADER = "HTTP_X_FORWARDED_FOR"
HTTP_USER_AGENT_HEADER = "HTTP_USER_AGENT"


JET_THEMES = [
    {
        "theme": "default",  # theme folder name
        "color": "#47bac1",  # color of the theme's button in user menu
        "title": "Default",  # theme title
    },
    {"theme": "green", "color": "#44b78b", "title": "Green"},
    {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
    {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
    {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
    {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
]


JET_INDEX_DASHBOARD = "jet.dashboard.dashboard.DefaultIndexDashboard"
JET_APP_INDEX_DASHBOARD = "jet.dashboard.dashboard.DefaultAppIndexDashboard"



CLOUDINARY_STORAGE = CLOUDINARY_STORAGE
DEFAULT_FILE_STORAGE = DEFAULT_FILE_STORAGE
