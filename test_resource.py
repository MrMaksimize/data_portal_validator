import pandas as pd
import simplejson as json
import requests
import io
import sauron.sauron as sauron

import unittest



class BaseResourceTest(unittest.TestCase):
    def setUp(self):
        print("SETUP")
        self.resource_url = None
        self.resource = None


    def tearDown(self):
        print('In tearDown()')
        self.resource_url = None
        del self.resource
        self.resource = None

    def test(self):
        print ('in test()')
        self.failUnlessEqual(self.fixture, range(1, 10))

#class SpecialEventsListResourceTest(BaseResourceTest):
#    def


if __name__ == '__main__':
    unittest.main()
