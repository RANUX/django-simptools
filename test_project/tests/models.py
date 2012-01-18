# -*- coding: UTF-8 -*-
from unittest.case import skip
from django.test import TestCase
from test_project.someapp.models import ModelWithRandomUID


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class RandomUIDAbstractModelTests(TestCase):

    @skip('Long time test')
    def test_random_uid_saving(self):
        COUNT = 100000
        for i in range(0, 100000):
            obj = ModelWithRandomUID.objects.create()
            self.assertIsNotNone(obj.uid)
        self.assertEquals(COUNT, ModelWithRandomUID.objects.count())


    def test_update_existing_object(self):
        obj = ModelWithRandomUID.objects.create()
        obj.save()
        uid = obj.uid
        self.assertIsNotNone(uid)
        self.assertFalse(obj.is_updated)

        obj = ModelWithRandomUID.objects.get(uid=uid)
        obj.is_updated=True
        obj.save()
        obj = ModelWithRandomUID.objects.get(uid=uid)
        self.assertTrue(obj.is_updated)

