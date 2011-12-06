# -*- coding: UTF-8 -*-
from django_simptools.money.fields import MoneyField
from django_simptools.money.widgets import CurrencySelectWidget

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


from django import forms

class MoneyForm(forms.Form):
    money = MoneyField(currency_widget=CurrencySelectWidget(choices=[("a","a")]))
