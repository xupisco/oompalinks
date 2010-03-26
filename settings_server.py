# -*- coding: utf-8 -*

import os, sys
ROOT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(ROOT_PATH, "apps"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/home/xupisco/www/xupisco/db/data.db'   # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

MEDIA_ROOT = os.path.join(ROOT_PATH, 'static')
MEDIA_URL = 'http://xupisco.tomada.us/static'
ADMIN_MEDIA_PREFIX = 'http://xupisco.tomada.us/media/admin/'

ROOT_URLCONF = 'urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "grappelli.context_processors.admin_url",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, "templates"),
    os.path.join(ROOT_PATH, "templates/admin"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'apps._cuco',
    'grappelli',
)