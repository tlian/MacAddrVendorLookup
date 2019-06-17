#!/usr/bin/python
import requests
import json
import sys


class LookupMacAddress(object):
    """
    Lookup Vendor information of a given macaddress
    """
    def __init__(self, api_key):
        self.baseuri = 'https://api.macaddress.io/v1?output=json&search='
        self.session = requests.session()
        self.session.headers.update({'X-Authentication-Token': api_key})
        self.session.verify = True

    def lookup_vendor(self, mac_address):
        """
        Look up vendor information of a given macaddress
        """
        uri = self.baseuri + mac_address
        response = self.session.get(uri)
        vendor_info = json.dumps(response.json())
        vendor_info = json.loads(vendor_info)
        try:
            print "Vendor company address of mac address {} is".format(
                mac_address)
            print vendor_info['vendorDetails']['companyAddress']
        except KeyError as exc:
            print exc
        except:
            print "Unexpected error:", sys.exc_info()[0]
