# -*- coding: utf-8 -*

import os, sys, socket, settings

try:
    if socket.gethostname() == "tomada":
        from settings_server import *
    else: 
        from settings_local import *
except ImportError:
    pass

ADMINS = (
    # Ordem alfabética... pra ninguém ficar triste!
    ('Leandro Voltolino', 'xupisco@gmail.com'),
)

PROJECT_NAME = "oompaLinks"
USE_GRAPPELLI = True
ROOT_PATH = os.path.dirname(__file__)

INTERNAL_IPS = ('127.0.0.1', )

#AUTH_PROFILE_MODULE = 'accounts.userprofile'

MANAGERS = ADMINS
SITE_ID = 1

ROOT_URLCONF = 'urls'
MEDIA_ROOT = os.path.join(ROOT_PATH, 'static')
MEDIA_URL = 'http://' + CURRENT_SERVER + '/static'

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'en_us' # Eu prefiro o admin em inglês, se quiser pode trocar!
USE_I18N = True
SECRET_KEY = 'x$8ok@bp1f00!&q=^&!t_zpv&52_l39rg$#67ptqd^=cuuz#r3'

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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ugettext = lambda s: s

LANGUAGES = (
    ('pt_br', ugettext(u'Português do Brasil')),
    ('en_us', ugettext(u'English')),
)

try:
    import grappelli
except ImportError:
    try:
        import apps.grappelli as grappelli
        sys.path.append(os.path.join(ROOT_PATH, "apps"))
    except ImportError:
        USE_GRAPPELLI = False

if USE_GRAPPELLI:
    GRAPPELLI_ADMIN_TITLE = getattr(settings, "GRAPPELLI_ADMIN_TITLE", PROJECT_NAME)
    ADMIN_MEDIA_PREFIX = 'http://' + CURRENT_SERVER + '/media/admin/'
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
    'grappelli',
    'debug_toolbar',
    'tagging'
)
