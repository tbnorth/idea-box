"""Base settings file; used by manage.py. All settings can be overridden via
local_settings.py"""
import logging
import os

from django.utils.crypto import get_random_string

# Stop South from spitting out debug messages during tests
logging.getLogger('south').setLevel(logging.CRITICAL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ideatest',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',  # Set to empty string for localhost
        'PORT': '',  # Set to empty string for default
    },
}

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

SITE_ID = 1

TEMPLATE_DIRS = (
    './templates',
)

INSTALLED_APPS = [
    'idea',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.staticfiles',
    'mptt',
    'core.custom_comments',  # from Collab
    'taggit',
]

ROOT_URLCONF = 'idea.example_urls'

DEBUG = True
STATIC_URL = '/static/'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_string(50))

COMMENTS_APP = 'core.custom_comments'

try:
    from local_settings import *
except ImportError:
    pass

MIDDLEWARE_CLASSES = (
'django.contrib.sessions.middleware.SessionMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware', 
'django.contrib.messages.middleware.MessageMiddleware'
)
