# -*- coding: UTF-8 -*-
"""
Created on May 7, 2011
@author: jake
"""
from unittest.case import skip

from  django.test import TestCase
from moneyed import Money
import moneyed
from test_project.someapp.models import ModelWithVanillaMoneyField, ModelRelatedToModelWithMoney

class VanillaMoneyFieldTestCase(TestCase):

    def test_saving(self):

        somemoney = Money("100.0")

        model = ModelWithVanillaMoneyField(money = somemoney)
        model.save()

        retrieved = ModelWithVanillaMoneyField.objects.get(pk=model.pk)

        self.assertEquals(somemoney.currency, retrieved.money.currency)
        self.assertEquals(somemoney, retrieved.money)

        # Try setting the value directly
        retrieved.money = Money(1, moneyed.DKK)
        retrieved.save()
        retrieved = ModelWithVanillaMoneyField.objects.get(pk=model.pk)

        self.assertEquals(Money(1, moneyed.DKK), retrieved.money)

    def test_exact_match(self):

        somemoney = Money("100.0")

        model = ModelWithVanillaMoneyField()
        model.money = somemoney

        model.save()
        
        retrieved = ModelWithVanillaMoneyField.objects.get(money=somemoney)
        self.assertEquals(model.pk, retrieved.pk)

    @skip("strange behaviour when save DecimalField with 2 places")
    def test_add_money_and_save(self):
        money = Money("10.45")
        expected = Money("10.76")
        model = ModelWithVanillaMoneyField(money=money)
        model.money = money + 3 % money
        model.save()
        self.assertEquals(expected, model.money)

    def test_range_search(self):

        minMoney = Money("3")

        model = ModelWithVanillaMoneyField(money = Money("100.0"))

        model.save()

        retrieved = ModelWithVanillaMoneyField.objects.get(money__gt=minMoney)
        self.assertEquals(model.pk, retrieved.pk)

        shouldBeEmpty = ModelWithVanillaMoneyField.objects.filter(money__lt=minMoney)
        self.assertEquals(shouldBeEmpty.count(), 0)

    def test_currency_search(self):

        otherMoney = Money("1000", moneyed.USD)
        correctMoney = Money("1000", moneyed.ZWN)

        model = ModelWithVanillaMoneyField(money = Money("100.0", moneyed.ZWN))
        model.save()

        shouldBeEmpty = ModelWithVanillaMoneyField.objects.filter(money__lt=otherMoney)
        self.assertEquals(shouldBeEmpty.count(), 0)

        shouldBeOne = ModelWithVanillaMoneyField.objects.filter(money__lt=correctMoney)
        self.assertEquals(shouldBeOne.count(), 1)


class RelatedModelsTestCase(TestCase):

    def test_find_models_related_to_money_models(self):

        moneyModel = ModelWithVanillaMoneyField(money = Money("100.0", moneyed.ZWN))
        moneyModel.save()

        relatedModel = ModelRelatedToModelWithMoney(moneyModel=moneyModel)
        relatedModel.save()

        ModelRelatedToModelWithMoney.objects.get(moneyModel__money = Money("100.0", moneyed.ZWN))
        ModelRelatedToModelWithMoney.objects.get(moneyModel__money__lt = Money("1000.0", moneyed.ZWN))