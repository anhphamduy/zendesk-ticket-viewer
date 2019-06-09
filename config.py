import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    TICKETS_PER_PAGE = 25
    PAGINATION_SIZE = 2

    ZENDESK_CREDS = {
        'email': os.environ.get('ZENDESK_EMAIL'),
        'password': os.environ.get('ZENDESK_PASSWORD'),
        'subdomain': os.environ.get('ZENDESK_SUBDOMAIN'),
    }


class DevelopmentConfig(Config):
    DEBUG = True
    ZENDESK_CREDS = {
        'email': os.environ.get('ZENDESK_DEV_EMAIL'),
        'password': os.environ.get('ZENDESK_DEV_PASSWORD'),
        'subdomain': os.environ.get('ZENDESK_DEV_SUBDOMAIN'),
    }


class TestingConfig(Config):
    TESTING = True

    ZENDESK_CREDS = {
        'email': os.environ.get('ZENDESK_TEST_EMAIL'),
        'password': os.environ.get('ZENDESK_TEST_PASSWORD'),
        'subdomain': os.environ.get('ZENDESK_TEST_SUBDOMAIN'),
    }

    ZENDESK_FAKE_CREDS = {
        'email': 'thisisnotalegitemail@outlook.com',
        'password': 'thispasswordiseasytoguess',
        'subdomain': 'thechildofadomain',
    }


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
