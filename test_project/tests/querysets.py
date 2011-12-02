# -*- coding: UTF-8 -*-
from django.test import TestCase
from test_project.someapp.models import SomeObject


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class ExtendedQuerySetTests(TestCase):

    def test_get_or_None(self):
        object = SomeObject.objects.create()
        self.assertIsNotNone(SomeObject.objects.get_or_None(pk=object.id))
