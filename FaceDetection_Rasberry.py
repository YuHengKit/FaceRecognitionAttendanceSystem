# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:51:15 2019

@author: Heng1222
"""
import cv2
import time
import requests
import datetime
import base64
import json

#import crop
#Set url of API
URL = 'http://127.0.0.1:8000/api/attendance/'       
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cam = cv2.VideoCapture(0)
cam.set(3, 320) # set video widht
cam.set(4, 240) # set video height
# Define min window size to be recognized as a face
minW = 0.2*cam.get(3)
minH = 0.2*cam.get(4)
while True:
    images = []
    ret, img =cam.read()
    img = cv2.flip(img, 1) # NO Flip vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Set image to grayscale
    faces = face_cascade.detectMultiScale( 
        gray,
        scaleFactor = 1.3,
        minNeighbors = 4,
        minSize = (int(minW), int(minH)),
       )
    #now = datetime.datetime.now()
    #print(now.hour)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if (faces is not None):
            #crop = crop(gray, x, y, w, h)
            name = 'temp' + '.png'
            cv2.imwrite(name, gray)
            with open(name, 'rb') as file:
                    images.append(base64.b64encode(file.read()).decode('utf-8'))
            date = time.mktime(datetime.datetime.now().timetuple())
            #print(date)
            data = {'images': images, 'date': date,'operation':100}
            response = requests.post(URL, json=data)
            #response.c
            print(response.status_code)
            if response.status_code == 201:         #if user recognized
                data = json.loads(response.text)    #read data from json file
                user = str(data['user'])            #read user's data
                print('{}: {}'.format(user, 'IN' if data['inout'] else 'OUT'))
            else:                                   #if user not recognized
                print('Unknown user')
            time.sleep(10)
    cv2.namedWindow('Face Detection', cv2.WINDOW_NORMAL)
    cv2.imshow('Face Detection',img)

    face=()        
    # Press 'ESC' for exiting video
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

#Do a bit of cleanup
print("\n [INFO] Exiting Program and cleaning-up stuff")
cam.release()
cv2.destroyAllWindows()      

