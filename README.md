##Veja bem... importante!

Você precisa ter o arquivo **settings_local.py** no root da aplicação, com as suas configurações. Abaixo um exmplo:

    # -*- coding: utf-8 -*

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    DATABASE_ENGINE = 'sqlite3'
    DATABASE_NAME = '/path/completo/para/o/banco.db'
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''
    DATABASE_HOST = ''
    DATABASE_PORT = ''

    CURRENT_SERVER = "127.0.0.1:8000"
    

##Dependências (so far...)

 * Grappelli: [http://code.google.com/p/django-grappelli/][1]
 * Debug-Toolbar: [http://github.com/robhudson/django-debug-toolbar][2]
 
[1]: http://code.google.com/p/django-grappelli/
[2]: http://github.com/robhudson/django-debug-toolbar