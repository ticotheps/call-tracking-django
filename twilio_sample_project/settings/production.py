'''
Production settings

- Set secret key from environment variable
'''

from .common import *
from decouple import config

SECRET_KEY = config('DJANGO_SECRET_KEY')

# Allow all hosts, so we can run on PaaS's like Heroku
ALLOWED_HOSTS = ['*']

# Configure the production database using dj_database_url
import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}
