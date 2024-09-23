"""
Django settings for builtwithdjango project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import cloudinary
import environ
import posthog
import sentry_sdk
import structlog
from posthog.sentry.posthog_integration import PostHogIntegration

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)
# reading .env file
environ.Env.read_env()

ENVIRONMENT = env("ENV")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

ADMIN_URL = env("ADMIN_URL")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.forms",
    "taggit",
    "django_extensions",
    "django_component",
    "django_filters",
    "rest_framework",
    "anymail",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.twitter",
    "cloudinary",
    "widget_tweaks",
    "django_q",
    "webpack_boilerplate",
    "djstripe",
    "robots",
    "pages.apps.PagesConfig",
    "projects.apps.ProjectsConfig",
    "jobs.apps.JobsConfig",
    "podcast.apps.PodcastConfig",
    "makers.apps.MakersConfig",
    "blog.apps.BlogConfig",
    "newsletter.apps.NewsletterConfig",
    "users.apps.UsersConfig",
    "api.apps.ApiConfig",
    "developers.apps.DevelopersConfig",
    "tools.apps.ToolsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "posthog.sentry.django.PosthogDistinctIdMiddleware",
    "kolo.middleware.KoloMiddleware",
]

ROOT_URLCONF = "builtwithdjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "builtins": [
                "django_component.templatetags",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "builtwithdjango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": env.db_url(),
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/build"),
]

WEBPACK_LOADER = {
    "MANIFEST_FILE": os.path.join(BASE_DIR, "frontend/build/manifest.json"),
}

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_REGION_NAME = "eu-east-1"
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = f"bwd-{ENVIRONMENT}"
# AWS_S3_FILE_OVERWRITE = False

MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Sites
SITE_ID = 1

if ENVIRONMENT == "prod":
    sentry_sdk.init(
        dsn=env("dsn"),
        integrations=[PostHogIntegration()],
    )

# Newsletters
EMAILOCTOPUS_API = env("EMAILOCTOPUS_API")
OCTO_LIST_ID = env("OCTO_LIST_ID")
REVUE_API_TOKEN = env("REVUE_API_TOKEN")
BUTTONDOWN_API_TOKEN = env("BUTTONDOWN_API_TOKEN")


INTERNAL_IPS = [
    "127.0.0.1",
]

AUTH_USER_MODEL = "users.CustomUser"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# config/settings.py
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": "mg.builtwithdjango.com",
}

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

DEFAULT_FROM_EMAIL = "Built with Django <rasul@builtwithdjango.com>"
SERVER_EMAIL = "error@builtwithdjango.com"

# Overriding the HTML of Built-In Widgets
# from Two Scoops of Django 3.x
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# django-allauth
# From django for professional book
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_FORMS = {
    "login": "users.forms.CustomLoginForm",
    "signup": "users.forms.CustomUserCreationForm",
}

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Stripe
STRIPE_LIVE_SECRET_KEY = env("STRIPE_LIVE_SECRET_KEY")
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY")
STRIPE_LIVE_MODE = env.bool("STRIPE_LIVE_MODE")
DJSTRIPE_WEBHOOK_VALIDATION = "retrieve_event"
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

# Cloudinary
cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"), api_key=env("CLOUDINARY_API_KEY"), api_secret=env("CLOUDINARY_API_SECRET")
)

# django-q
Q_CLUSTER = {
    "name": "builtwithdjango-q",
    "timeout": 90,
    "retry": 120,
    "workers": 4,
    "max_attempts": 2,
    "redis": env("REDIS_URL"),
}

# Screenshot API
SCREENSHOT_API_KEY = env("SCREENSHOT_API_KEY")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(),
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(),
        },
        "key_value": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.KeyValueRenderer(key_order=["timestamp", "level", "event", "logger"]),
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
            "level": "DEBUG",
        },
        "json_console": {
            "class": "logging.StreamHandler",
            "formatter": "json_formatter",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "django_structlog": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "builtwithdjango": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

if ENVIRONMENT == "prod":
    LOGGING["loggers"]["builtwithdjango"]["level"] = env("DJANGO_LOG_LEVEL", default="INFO")
    LOGGING["loggers"]["builtwithdjango"]["handlers"] = ["json_console"]
    LOGGING["loggers"]["django_structlog"]["handlers"] = ["json_console"]

posthog.project_api_key = env("POSTHOG_API_KEY")
posthog.host = "https://app.posthog.com"
if DEBUG:
    posthog.debug = True

POSTHOG_DJANGO = {"distinct_id": lambda request: request.user and request.user.distinct_id}

if DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": env("REDIS_URL"),
        }
    }

TJ_ALERTS_HOST = "https://gettjalerts.com/api"
TJ_ALERTS_API_KEY = env("TJ_ALERTS_API_KEY")

HEALTHCHECKS_HOST = "https://healthchecks.cr.lvtd.dev/ping"
