import pandas as pd
import simplejson as json
import requests
import io
import sauron.sauron as sauron

import resource

class Dataset(object):
    def __init__(self, id):
        self.id = id;
        self.url = "http://data.sandiego.gov/api/3/action/package_show?id=" + id
        self.resources = []
        self.groups = []
        metadata = requests.get(self.url)
        metadata = json.loads(metadata.text)
        metadata = json.loads(json.dumps(metadata['result']))[0]

        self.metadata = metadata

        for r in metadata["resources"]:
            self.resources.append(resource.Resource(r))


        #for g in metadata["groups"]:
            #self.groups.append(resource.Resource(g))
