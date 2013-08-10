from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elmo',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
            'charset' : 'utf8',
            'use_unicode' : True,
        },
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    },
}

REPOSITORY_BASE = '/data/l10n/stage/stage/repos'

TRANSPORT = 'amqp://guest:guest@localhost:5672//'

# if you want to test the Sentry
#RAVEN_CONFIG = {
#    'dsn': 'http://user:pw@localhost:9000/2'  # see api keys on your local sentry install
#}
