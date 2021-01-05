import numpy as np

import cv2
from cv2 import *
import time

cam = cv2.VideoCapture(0)


haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while True:
    _,img = cam.read()
   
 
    cv2.imwrite("User." + str(face_id) + '.' + str(count) + ".jpg", img)
    ##cv2.imshow('image', img)
    
        
    ch = cv2.waitKey(100)
    if ch& 0xFF == ord('q'):
        break
    elif count >=2:
        break
    
    count+=1
    
    print("Waiting .....")
    time.sleep(5)

        
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()