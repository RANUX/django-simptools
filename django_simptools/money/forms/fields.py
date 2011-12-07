# -*- coding: UTF-8 -*-
'''
@author: Jacob Hansson <jacob@voltvoodoo.com>
@site: https://github.com/jakewins/django-money
@license: BSD
'''
import re
from django.core.validators import RegexValidator

__all__ = ('MoneyField',)

from django.utils.translation import ugettext_lazy as _
from django import forms
from widgets import InputMoneyWidget
from moneyed.classes import Money, CURRENCIES, DEFAULT_CURRENCY_CODE

__all__ = ('MoneyField',)

class MoneyField(forms.DecimalField):

    def __init__(self, currency_widget=None, validators=[RegexValidator(re.compile(r'^[0-9]+(\.[0-9]{0,2})?$'))], *args, **kwargs):
        self.widget = InputMoneyWidget(currency_widget=currency_widget)
        super(MoneyField, self).__init__(validators=validators, *args, **kwargs)

    def to_python(self, value):
        if not isinstance(value, tuple):
            raise Exception("Invalid money input, expected sum and currency.")

        amount = super(MoneyField, self).to_python(value[0])
        currency = value[1]
        if not currency:
            raise forms.ValidationError(_(u'Currency is missing'))
        currency = currency.upper()
        if not CURRENCIES.get(currency, False) or currency == DEFAULT_CURRENCY_CODE:
            raise forms.ValidationError(_(u"Unrecognized currency type '%s'." % currency))
        return Money(amount=amount, currency=currency)

    def validate(self, value):
        if not isinstance(value, Money):
            raise Exception("Invalid money input, expected Money object to validate.")

        super(MoneyField, self).validate(value.amount)


    def run_validators(self, value):

        if not isinstance(value, Money):
            raise Exception("Invalid money input, expected Money object to validate.")

        super(MoneyField, self).run_validators(value.amount)


