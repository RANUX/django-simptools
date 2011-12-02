# -*- coding: UTF-8 -*-
from django.db import models


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class ChainableQuerySetManager(models.Manager):
    '''
    More info can be found at http://djangosnippets.org/snippets/562/
    '''
    def __init__(self, qs_class=models.query.QuerySet):
        super(ChainableQuerySetManager,self).__init__()
        self.queryset_class = qs_class

    def get_query_set(self):
        return self.queryset_class(self.model)

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)