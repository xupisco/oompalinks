# -*- coding: utf-8 -*

import socket, settings
from app_config import *

APP_ENV = "development"

if socket.gethostname() == "tomada":
    APP_ENV = "production"
        
ADMINS = (
    # Ordem alfabética... pra ninguém ficar triste!
    ('Leandro Voltolino', 'xupisco@gmail.com'),
)

PROJECT_NAME = "oompaLinks"
GRAPPELLI_ADMIN_TITLE = getattr(settings, "GRAPPELLI_ADMIN_TITLE", PROJECT_NAME)
INTERNAL_IPS = ('127.0.0.1', )


TEMPLATE_DEBUG = APP_CONFIG[APP_ENV]['debug']

DATABASE_ENGINE =   APP_CONFIG[APP_ENV]['database']['engine']   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME =     APP_CONFIG[APP_ENV]['database']['name']     # Or path to database file if using sqlite3.
DATABASE_USER =     APP_CONFIG[APP_ENV]['database']['user']     # Not used with sqlite3.
DATABASE_PASSWORD = APP_CONFIG[APP_ENV]['database']['password'] # Not used with sqlite3.
DATABASE_HOST =     APP_CONFIG[APP_ENV]['database']['host']     # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT =     APP_CONFIG[APP_ENV]['database']['port']     # Set to empty string for default. Not used with sqlite3.

CURRENT_SERVER = APP_CONFIG[APP_ENV]['server']['host']

MEDIA_ROOT = os.path.join(ROOT_PATH, 'static')
MEDIA_URL = 'http://' + CURRENT_SERVER + '/static'
ADMIN_MEDIA_PREFIX = 'http://' + CURRENT_SERVER + '/media/admin/'

MEDIA_ROOT = os.path.join(ROOT_PATH, 'static')
MEDIA_URL = 'http://xupisco.tomada.us/static'
ADMIN_MEDIA_PREFIX = 'http://xupisco.tomada.us/media/admin/'

ROOT_URLCONF = 'urls'
#AUTH_PROFILE_MODULE = 'accounts.userprofile'

MANAGERS = ADMINS
SITE_ID = 1

ugettext = lambda s: s

LANGUAGES = (
    ('pt_br', ugettext(u'Português do Brasil')),
    ('en_us', ugettext(u'English')),
)

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'en_us' # Eu prefiro o admin em inglês, se quiser pode trocar!
USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x$8ok@bp1f00!&q=^&!t_zpv&52_l39rg$#67ptqd^=cuuz#r3'

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
    'grappelli',
)
