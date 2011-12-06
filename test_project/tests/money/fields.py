# -*- coding: UTF-8 -*-
from django.test import TestCase
from moneyed.classes import Money, CURRENCIES
from decimal import Decimal
from test_project.someapp.forms import MoneyForm


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class MoneyFormTestCase(TestCase):

    def test_render(self):

        form = MoneyForm()
        expected = """<tr><th><label for="id_money">Money:</label></th><td><input type="text" name="money" /><select name="money_currency">
<option value="a">a</option>
</select></td></tr>"""

        self.assertEquals(str(form), expected)

    def test_validate(self):
        SEK_currency = CURRENCIES['SEK']
        form = MoneyForm({"money":"10", "money_currency":SEK_currency.code})
        self.assertTrue(form.is_valid())
        result = form.cleaned_data['money']
        self.assertTrue(isinstance(result, Money))
        self.assertEquals(result.amount, Decimal("10"))
        self.assertEquals(result.currency, SEK_currency)

    def test_non_existant_currency(self):
        form = MoneyForm({"money":"10", "money_currency":"_XX!123_"})
        self.assertFalse(form.is_valid())
        self.assertEquals({'money': [u"Unrecognized currency type '_XX!123_'."]}, form.errors)


