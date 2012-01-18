# -*- coding: UTF-8 -*-
from django.test import TestCase


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class BaseViewTestCase(TestCase):

    def assertContainsTextItems(self, response, items=[]):
        for item in items:
            self.assertContains(response, item)

class AuthorizedViewTestCase(BaseViewTestCase):
    username = 'admin'
    password = '12345'

    def setUp(self):
        self.client_login()

    def client_login(self, username='', password=''):
        self.auth = {
            "username": username if username else self.username,
            "password": password if password else self.password,
        }
        is_logged = self.client.login(**self.auth)
        self.assertTrue(is_logged)

    def tearDown(self):
        self.client.logout()