# -*- coding: UTF-8 -*-
from django_simptools.money.fields import MoneyField
from django_simptools.money.widgets import CurrencySelectWidget
from django import forms
from test_project.someapp.models import ModelWithVanillaMoneyField

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'




class MoneyForm(forms.Form):
    money = MoneyField(
        currency_widget=CurrencySelectWidget(choices=[("a","a")])
    )

class MoneyModelForm(forms.ModelForm):

    class Meta:
        model = ModelWithVanillaMoneyField