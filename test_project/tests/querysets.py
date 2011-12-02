# -*- coding: UTF-8 -*-
from unittest.case import skip
from django.test import TestCase
from test_project.someapp.models import SomeObject, ParentObject


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class ExtendedQuerySetTests(TestCase):

    def setUp(self):
        self.parent = ParentObject.objects.create()
        self.object = SomeObject.objects.create(parent=self.parent)

    def test_get_or_None(self):
        self.assertIsNotNone(SomeObject.objects.all().get_or_None(pk=self.object.id))

    def test_count_related_someobjects(self):
        self.assertEquals(1, self.parent.count_someobjects())

    @skip('Causes recursion!:(')
    def test_create_related_someobject(self):
        # be careful, it causes
        # RuntimeError: maximum recursion depth exceeded while calling a Python object
        someobject = self.parent.create_someobject()
        
