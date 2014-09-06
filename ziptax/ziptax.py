# -*- coding: utf-8 -*-
import requests
import logging

log = logging.getLogger(__name__)


ZIPTAX_API_KEY = ''
ZIPTAX_URL_SUBDOMAIN = 'api.zip-tax.com'
ZIPTAX_URL_ACTIONS = 'request'
ZIPTAX_URL_VERSION = 'v20'

URL = 'http://{0}/{1}/{2}'.format(
    ZIPTAX_URL_SUBDOMAIN, ZIPTAX_URL_ACTIONS, ZIPTAX_URL_VERSION)

# Response codes
RESPONSE_CODES = {
    100: 'Successful API Requet',
    101: 'Key format is not valid',
    102: 'State format is not valid',
    103: 'City format is not valid',
    104: 'Postal code format is not valid',
    105: 'Query string format is not valid'
}


class ZipTaxResponseError(Exception):
    def __init__(self):
        self.value = RESPONSE_CODES.get(self.code)

    def __str__(self):
        return repr(self.value)


class InvalidKey(ZipTaxResponseError):
    code = 101


class InvalidState(ZipTaxResponseError):
    code = 102


class InvalidCity(ZipTaxResponseError):
    code = 103


class InvalidPostalcode(ZipTaxResponseError):
    code = 104


class InvalidFormat(ZipTaxResponseError):
    code = 105


class ZipTaxError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class ZipTaxInfo(object):
    def __init__(self, data):
        self.data = data

    def __getattr__(self, attr):
        if attr == 'results':
            results = []
            for i in self.data[attr]:
                results.append(ZipTaxInfo(i))
            return results
        return self.data[attr]


class ParamValidation(object):
    def __init__(self, *args, **kwargs):
        pass


class ZipTax(object):
    def __init__(self, key, url=URL):
        self.url = url
        self.key = key
        self.params = {}

    def get(self, zipcode, state='', city=''):
        self.params.update({'key': self.key, "format": 'JSON',
                            'postalcode': zipcode, 'state': state, 'city': city})
        req = requests.get(self.url, params=self.params)

        # Get python dict
        data = req.json()

        # Get response code
        code = data.get('rCode', 0)

        # Success code
        if code == 100:
            return ZipTaxInfo(data)

        # Error codes
        if code == 101:
            raise InvalidKey()
        if code == 102:
            raise InvalidState()
        if code == 103:
            raise InvalidCity()
        if code == 104:
            InvalidPostalcode()
        if code == 105:
            InvalidFormat()

        raise ZipTaxError('Unknown Error')
