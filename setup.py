# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.2'

setup(
    version=VERSION,
    packages=find_packages(),
    name='django_simptools',
    author='Razzhivin Alexander',
    author_email='admin@httpbots.com',
    description='django_simptools is a suit with useful functions for daily usage',
    url='http://github.com/RANUX/django_simptools',
    license = 'LGPL',
    platforms=['any'],
    include_package_data=True,
    test_suite='tests',
    tests_require=['nose','django', 'django_nose', 'py-moneyed', ]
)
