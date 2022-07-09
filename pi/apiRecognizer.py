import requests
import time
import os
from pprint import pprint

uploadImage = "kfz2.jpg"

def lookupPlate(image):
    regions = ['de']
    with open('images/'+image, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions), 
            files=dict(upload=fp),
            headers={'Authorization': 'Token 5e52f71a0abd5e1c22900d2882effd115a058ab8'})
    return response

st = time.time()
response = lookupPlate(uploadImage)
et = time.time()

jsonResponse = response.json()
pprint(jsonResponse)
print('\n')
print('Image: ' + os.path.abspath("images/" + uploadImage))
print('Request time:', et - st, 'seconds')
print('Plate:', jsonResponse['results'][0]['candidates'][0]['plate'])
