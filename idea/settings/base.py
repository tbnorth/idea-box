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

INSTALLED_APPS = [
    'idea',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'mptt',
    'taggit',
    'debug_toolbar',
    'debug_panel'
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
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'debug_panel.middleware.DebugPanelMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG
        },
    },
]
