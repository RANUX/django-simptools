# -*- coding: UTF-8 -*-
from django.db import models
from django_simptools.managers import ChainableQuerySetManager
from django_simptools.querysets import ExtendedQuerySet


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class SomeObject(models.Model):
    objects = ChainableQuerySetManager(ExtendedQuerySet)