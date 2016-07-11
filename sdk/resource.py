import pandas as pd
import simplejson as json
import requests
import io
import sauron.sauron as sauron

class Resource(object):
    def __init__(self, resourceDict):
        self.id = resourceDict["id"]
        self.file_uri = resourceDict["url"]
        self.metadata = resourceDict
        #self.data = self.loadData()
        self.data = None

    def loadData(self):
        s = requests.get(self.file_uri).content
        self.data = pd.read_csv(io.StringIO(s.decode('utf-8')))
