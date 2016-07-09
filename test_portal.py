import pandas as pd
import simplejson as json
import requests
import io
import sauron.sauron as sauron

import unittest


class PortalTest(unittest.TestCase):
    def setUp(self):
        print('In setUp()')
        dataListUrl = "http://data.sandiego.gov/api/3/action/current_package_list_with_resources"
        dataList = requests.get(dataListUrl)
        dataList = json.loads(dataList.text)
        dataList = json.loads(json.dumps(dataList['result']))[0]


def tearDown(self):
    print
    'In tearDown()'


# del self.fixture

def test(self):
    print
    'in test()'
# self.failUnlessEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
    unittest.main()


# %%

# for i in dataList:
#    print(i)

# dataset = dataList[41]
# resource_url = dataset["resources"][0]["url"]
# s = requests.get(resource_url).content

# file = pd.read_csv(io.StringIO(s.decode('utf-8')))



# validator = sauron.dispoCodeValidator()
# print(validator.is_valid(file))
