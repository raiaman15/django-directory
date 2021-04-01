from config.settings.base import *
from config.settings.base import env

# Production specific settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env.str("DJANGO_ALLOWED_HOSTS").split(" ")

# ADMINS = [
#     (
#         env.str("WEBMASTER_NAME", default="Webmaster"),
#         env.str("WEBMASTER_EMAIL", default="webmaster@test.infroid.com")
#     ),
#     (
#         env.str("ADMINISTRATOR_NAME", default="Administrator"),
#         env.str("ADMINISTRATOR_EMAIL", default="administrator@test.infroid.com")
#     )
# ]
# MANAGERS = ADMINS

# Add INSTALLED_APPS on top
INSTALLED_APPS = [] + INSTALLED_APPS
# Add INSTALLED_APPS at bottom
INSTALLED_APPS += ['admin_honeypot', ]

# Add MIDDLEWARE on top
MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware', ] + MIDDLEWARE
# Add MIDDLEWARE at bottom
MIDDLEWARE += ['django.middleware.cache.FetchFromCacheMiddleware', ]

ROOT_URLCONF = 'config.urls.production'

WSGI_APPLICATION = 'config.wsgi.application'

# django-allauth config
# FIX-URGENT: Change to production specific email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cache config
CACHE_MIDDLEWARE_ALIAS = 'default'
# TODO-NORMAL: Update to 7 days once working properly
CACHE_MIDDLEWARE_SECONDS = 3600
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Security config
if env.bool("MIMIC_PRODUCTION_LOCALLY"):
    pass
else:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # TODO-NORMAL: Update to 7 days or 30 days once working properly
    SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=60)
    SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
    SECURE_CONTENT_TYPE_NOSNIFF = True

# Admin Honeypot config
ADMIN_HONEYPOT_EMAIL_ADMINS = True

# Anymail
# TODO-NORMAL: Remove console backend and switch to Twilio Sendgrid
# EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
# ANYMAIL = {
#     "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),
#     "SENDGRID_GENERATE_MESSAGE_ID": env("SENDGRID_GENERATE_MESSAGE_ID"),
#     "SENDGRID_MERGE_FIELD_FORMAT": env("SENDGRID_MERGE_FIELD_FORMAT"),
#     "SENDGRID_API_URL": env("SENDGRID_API_URL", default="https://api.sendgrid.com/v3/"),
# }
