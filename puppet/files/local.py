from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/src/l10n/a10n/a10n/settings/db.sql',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    },
}
REPOSITORY_BASE = '/home/vagrant/stage/repos/'

TRANSPORT = 'amqp://guest:guest@localhost:5672//'

# if you want to test the Sentry
#RAVEN_CONFIG = {
#    'dsn': 'http://user:pw@localhost:9000/2'  # see api keys on your local sentry install
#}
