About
============
Django-simptools is a library with useful functions/classes for daily usage.

Dependencies
============
See requirements file::

    pip install -r requirements

Installation
============
Installation from github::

    pip install -e git+https://github.com/RANUX/django-simptools#egg=django-simptools

money.MoneyField
============
Example::

    CURRENCY_CHOICES = [(CURRENCIES['RUB'].code, CURRENCIES['RUB'].name)]

    class MoneyForm(forms.Form):
        money = MoneyField(currency_widget=CurrencySelectWidget(choices=CURRENCY_CHOICES))

Testing
============
Go to django-simptools directory and run tests::

    $ cd test_project/
    $ python manage.py test tests


Contributing
============
The source is available on `GitHub <http://github.com/RANUX/django-simptools>`_ - to
contribute to the project, fork it on GitHub and send a pull request, all
contributions and suggestions are welcome!