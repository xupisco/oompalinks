# -*- coding: utf-8 -*

import socket, settings

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
GRAPPELLI_ADMIN_TITLE = getattr(settings, "GRAPPELLI_ADMIN_TITLE", PROJECT_NAME)
INTERNAL_IPS = ('127.0.0.1', )

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
