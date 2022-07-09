import requests
from pprint import pprint
regions = ['de']
with open('images/kfz.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions), 
        files=dict(upload=fp),
        headers={'Authorization': 'Token 5e52f71a0abd5e1c22900d2882effd115a058ab8'})
pprint(response.json())