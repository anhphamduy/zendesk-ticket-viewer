import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LANGUAGES = ['en', 'es']
    TICKETS_PER_PAGE = 25
    PAGINATION_SIZE = 2

    ZENDESK_CREDS = {
        'email': os.environ.get('ZENDESK_EMAIL'),
        'password': os.environ.get('ZENDESK_PASSWORD'),
        'subdomain': os.environ.get('ZENDESK_SUBDOMAIN'),
    }
