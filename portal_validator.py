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

file = pd.read_csv(io.StringIO(s.decode('utf-8')))
#%%
# Validator Class
class baseDFValidator(pv.DataFrameValidator):
    min_row_num = None
    ## Override the class to allow a min row number
    def _check_dataframe_size(self, df):
        if self.column_num is not None and len(df.columns) != self.column_num:
            raise pv.core.exceptions.ValidationError('DataFrame columns number is not %s'
                                  % self.column_num)

        if self.row_num is not None and len(df.index) != self.row_num:
            raise pv.core.exceptions.ValidationError('DataFrame rows number is not %s'
                                  % self.row_num)
        
        if self.min_row_num is not None and len(df.index) < self.min_row_num:
            raise pv.core.exceptions.ValidationError('DataFrame rows number less than %s'
                                  % self.row_num)

# Validator for Dispo Code Files Only

class dispoCodeValidator(baseDFValidator):
    min_row_num = 40
    dispo_code = pv.CharColumnValidator('dispo_code')
    description = pv.CharColumnValidator('description')
    

    
#%%

validator = dispoCodeValidator()
validator.is_valid(file)


