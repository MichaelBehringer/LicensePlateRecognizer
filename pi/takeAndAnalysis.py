import cv2
from datetime import datetime
import numpy
import requests
import time
import os
from pprint import pprint

stCapture = time.time()
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

ret, image = cam.read()

scale = 0.5 
frame_darker = (image * scale).astype(numpy.uint8)

now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S")

path = 'camera/img_'+dt_string+'.jpg'

cv2.imwrite(path, frame_darker)
cam.release()
cv2.destroyAllWindows()
etCapture = time.time()

def lookupPlate(image):
    regions = ['de']
    with open(image, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions), 
            files=dict(upload=fp),
            headers={'Authorization': 'Token 5e52f71a0abd5e1c22900d2882effd115a058ab8'})
    return response

stLookup = time.time()
response = lookupPlate(path)
etLookup = time.time()

jsonResponse = response.json()
pprint(jsonResponse)
print('\n')
print('Image: ' + os.path.abspath(path))
print('Capture time:', etCapture - stCapture, 'seconds')
print('Lookup time:', etLookup - stLookup, 'seconds')
print('Plate:', jsonResponse['results'][0]['candidates'][0]['plate'])