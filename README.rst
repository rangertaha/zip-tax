
===========
Zip-tax
===========

A client library for `Zip-Tax.com <http://www.zip-tax.com>`_. sales tax `API <http://docs.zip-tax.com/en/latest>`_.

Typical usage::

    #!/usr/bin/env python

    import ziptax

    ZIPTAX_API_KEY = 'XXXXXXXX'

    ztax = ziptax.ZipTax(ZIPTAX_API_KEY)

    # Returns data for postalcode: 12345
    data = ztax.get(12345)

    # Printing the the various fields
    print 'Version:', data.version
    print 'rCode', data.rCode
    for i in data.results:
        print i.geoPostalCode
        print i.geoCity
        print i.geoCounty
        print i.geoState
        print i.taxSales
        print i.taxUse
        print i.txbService
        print i.txbFreight
        print i.stateSalesTax
        print i.stateUseTax
        print i.citySalesTax
        print i.cityUseTax
        print i.cityTaxCode
        print i.countySalesTax
        print i.countyUseTax
        print i.countyTaxCode
        print i.districtSalesTax
        print i.districtUseTax




Installation
============

**Automatic installation**::

    pip install ziptax

Zip-tax is listed in PyPI and can be installed with pip or easy_install.



**Manual installation**: Download the latest source from `PyPI
<https://pypi.python.org/pypi/zip-tax>`_.

.. parsed-literal::

    tar xvzf zip-tax-$VERSION.tar.gz
    cd ziptax-$VERSION
    python setup.py build
    sudo python setup.py install

The Zip-tax source code is `hosted on GitHub <https://github.com/rangertaha/zip-tax>`_.



TODO
====

* Write tests
* Validate input parameters
* Handle empty results.

