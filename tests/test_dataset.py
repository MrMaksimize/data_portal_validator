import pandas as pd
import simplejson as json
import requests
import io
import sauron.sauron as sauron
import sdk.dataset as dataset

import unittest


## Tests that apply to all datasets;

class BaseDatasetTest(unittest.TestCase):

    datasetID = "d389196b-991d-4b93-afab-cb8c6c9bfd56"

    def setUp(self):
        #print("setUp")
        self.dataset = dataset.Dataset(self.datasetID)
        #self.dataset.loadResourceData()

    def test_is_published(self):
        #print ('test_is_published')
        self.assertEqual(self.dataset.metadata['private'], "Published")

    def test_multiple_resources(self):
        self.assertGreater(len(self.dataset.resources), 1)

    def tearDown(self):
        #print('tearDown')
        del self.dataset
        self.dataset = None


class SpecialEventsDatasetTest(BaseDatasetTest):
    datasetID = "d389196b-991d-4b93-afab-cb8c6c9bfd56"



if __name__ == '__main__':
    unittest.main()
