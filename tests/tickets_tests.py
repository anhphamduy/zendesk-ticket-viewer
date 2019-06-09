import re

from snapshottest import TestCase
from zenpy import Zenpy

from app import create_app


class FlaskClientTestCase(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_tickets_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.get_data())

        response = self.client.get('/tickets')
        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.get_data())

        # reintialise zenpy client with a fake credential
        self.app.zenpy = Zenpy(**self.app.config['ZENDESK_FAKE_CREDS'])

        response = self.client.get('/')
        self.assertEqual(response.status_code, 503)
        self.assertMatchSnapshot(response.get_data())

        response = self.client.get('/tickets')
        self.assertEqual(response.status_code, 503)
        self.assertMatchSnapshot(response.get_data())

    def test_single_ticket_page(self):
        response = self.client.get('/tickets/1')
        self.assertEqual(response.status_code, 200)
        self.assertMatchSnapshot(response.get_data())

        response = self.client.get('/tickets/103928102381092389123')
        self.assertEqual(response.status_code, 503)
        self.assertMatchSnapshot(response.get_data())
