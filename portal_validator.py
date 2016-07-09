import pandas as pd
import pandas_validator as pv

import simplejson as json
import requests
import io

dataListUrl = "http://data.sandiego.gov/api/3/action/current_package_list_with_resources"

dataList = requests.get(dataListUrl)
dataList = json.loads(dataList.text)
dataList = json.loads(json.dumps(dataList['result']))[0]
#%%

#for i in dataList:
#    print(i)
                                
dataset = dataList[41]
resource_url = dataset["resources"][0]["url"]
s = requests.get(resource_url).content

c = pd.read_csv(io.StringIO(s.decode('utf-8')))
#%%
# Validate Columns

