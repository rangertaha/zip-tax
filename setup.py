# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='zip-tax',
    version='0.0.1',
    author='Rangertaha',
    author_email='rangertaha@gmail.com',
    packages=['ziptax'],
    scripts=[],
    url='http://pypi.python.org/pypi/zip-tax',
    license='LICENSE.txt',
    description='API zip-tax.com sales tax service',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.0.1",
    ],
)
