from config.settings.base import *
from config.settings.base import env


# Development specific settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.str("DJANGO_ALLOWED_HOSTS").split(" ")

ADMINS = [
    (
        env.str("WEBMASTER_NAME", default="Webmaster"),
        env.str("WEBMASTER_EMAIL", default="webmaster@test.infroid.com")
    ),
    (
        env.str("ADMINISTRATOR_NAME", default="Administrator"),
        env.str("ADMINISTRATOR_EMAIL", default="administrator@test.infroid.com")
    )
]
MANAGERS = ADMINS

# Add INSTALLED_APPS on top
INSTALLED_APPS = [] + INSTALLED_APPS
# Add INSTALLED_APPS at bottom
INSTALLED_APPS += ['django_extensions', ]

# Add MIDDLEWARE on top
MIDDLEWARE = [] + MIDDLEWARE
# Add MIDDLEWARE at bottom
MIDDLEWARE += []

ROOT_URLCONF = 'config.urls.local'

WSGI_APPLICATION = 'config.wsgi.application'

# django-allauth config
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-extensions
# runserver_plus
RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8000'
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}
# Truncate SQL queries to this many characters (None means no truncation)
RUNSERVER_PLUS_PRINT_SQL_TRUNCATE = 1000
# After how many seconds auto-reload should scan for updates in poller-mode
RUNSERVERPLUS_POLLER_RELOADER_INTERVAL = 2
# Werkzeug reloader type [auto, watchdog, or stat]
RUNSERVERPLUS_POLLER_RELOADER_TYPE = 'auto'
# Add extra files to watch
RUNSERVER_PLUS_EXTRA_FILES = []
