# -*- coding: utf-8 -*

import os, sys
ROOT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(ROOT_PATH, "complink"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/Users/leandro/Sites/complink/db/data.db'   # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

CURRENT_SERVER = "127.0.0.1:8000"
CURRENT_SERVER = "192.168.1.201:8000"
USE_GRAPPELLI = True

MEDIA_ROOT = os.path.join(ROOT_PATH, 'static')
MEDIA_URL = 'http://' + CURRENT_SERVER + '/static'

if USE_GRAPPELLI:
    ADMIN_MEDIA_PREFIX = 'http://' + CURRENT_SERVER + '/media/admin/'

ROOT_URLCONF = 'urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

if USE_GRAPPELLI:
    TEMPLATE_DIRS = (
        os.path.join(ROOT_PATH, "templates"),
        os.path.join(ROOT_PATH, "templates/admin"),
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'apps.links',
    #'tagging',
    'grappelli',
)

if os.path.exixts('apps/grappelli'):
    INSTALLED_APPS.append('apps/grappelli')
else 
    INSTALLED_APPS.append('grappelli')
