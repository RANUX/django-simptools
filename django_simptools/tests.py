# -*- coding: UTF-8 -*-
from django.test import TestCase


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class AuthorizedViewTestCase(TestCase):
    username = 'admin'
    password = '12345'

    def setUp(self):
        self.client_login()

    def client_login(self, username='admin', password='12345'):
        self.auth = {
            "username": self.username if self.username else username,
            "password": self.password if self.password else password,
        }
        is_logged = self.client.login(**self.auth)
        self.assertTrue(is_logged)

    def tearDown(self):
        self.client.logout()