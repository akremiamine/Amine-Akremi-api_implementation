


import json
import requests


url = 'http://127.0.0.1:8000//ML_prediction'

input_data_for_model = {
    
    'wconfid' : 5,
    'pctid' : 166,

    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)


