APP_CONFIG = (
    'development': (
        'database': (
            'engine': 'sqlite3',
            'name': 'db/data.db',
            'user': '',
            'password': '',
            'host': '',
            'port': '',
        ),

        'server': (
            'host': '127.0.0.1:8000',
        ),

        'debug': True
    ),

    'production': (
        'database': (
            'engine': 'sqlite3',
            'name': 'db/data.db',
            'user': '',
            'password': '',
            'host': '',
            'port': '',
        ),

        'server': (
            'host': '127.0.0.1:8000',
        ),

        'debug': True
         
    )
)
