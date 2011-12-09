# -*- coding: UTF-8 -*-
from random import randint
from django.db import models, transaction
from django.db import IntegrityError
from django.utils.translation import ugettext_lazy as _

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'



class RandomUIDAbstractModel(models.Model):
    """
    An abstract base class model that provides positive random uid field.
    """
    MAX_UID = 2147483647

    uid = models.PositiveIntegerField(_('unique id'), unique=True, editable=False)

    class Meta:
        abstract = True

    @transaction.commit_manually
    def save(self, *args, **kwargs):
        while self.pk is None:
            try:
                random_uid = randint(1, self.MAX_UID)
                self.uid = random_uid
                super(RandomUIDAbstractModel, self).save(*args, **kwargs)
            except IntegrityError:
                transaction.rollback()
        transaction.commit()


