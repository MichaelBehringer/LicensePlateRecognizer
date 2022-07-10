import cv2
from datetime import datetime
import numpy

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

ret, image = cam.read()

scale = 0.5  # whatever scale you want
frame_darker = (image * scale).astype(numpy.uint8)

now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S")

path = 'camera/img_'+dt_string+'.jpg'

cv2.imwrite(path, frame_darker)
#cv2.imwrite(path, image)
cam.release()
cv2.destroyAllWindows()

print(path + ' created')