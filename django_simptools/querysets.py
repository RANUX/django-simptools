# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class ExtendedQuerySet(models.query.QuerySet):

    def get_or_None(self, *args, **kwargs):
        result = None
        try:
            result = self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            pass
        return result