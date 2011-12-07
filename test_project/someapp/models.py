# -*- coding: UTF-8 -*-
from django.db import models
from django_simptools.managers import ChainableQuerySetManager
from django_simptools.money.models.fields import MoneyField
from django_simptools.querysets import ExtendedQuerySet


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class ParentObject(models.Model):
    value = models.IntegerField(default=0)

    def count_someobjects(self):
        return self.someobjects.count()

    def create_someobject_throw_related(self):
        return self.someobjects.create()

    def create_someobject(self):
        return SomeObject.objects.create(parent=self)

class SomeObject(models.Model):
    parent = models.ForeignKey(ParentObject, related_name='someobjects')
    value = models.IntegerField(default=1)
    objects = ChainableQuerySetManager(ExtendedQuerySet)


# ----------------- For Money Tests ------------

class ModelWithVanillaMoneyField(models.Model):
    money = MoneyField(max_digits=10, decimal_places=2)

class ModelRelatedToModelWithMoney(models.Model):
    moneyModel = models.ForeignKey(ModelWithVanillaMoneyField)