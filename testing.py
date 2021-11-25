import numpy as np
import cv2
import serial
import time
var='0'

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
#fire_detection.xml file & this code should be in the same folder while running the code

ser1 = serial.Serial('COM4',9600)#change COM port number on which your arduino is connected

cap = cv2.VideoCapture(0)
while 1:
    #ser1.write('0')
    ret, img = cap.read()
    #cv2.imshow('imgorignal',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img,1.2,3)
    for (x,y,w,h) in fire:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print('Fire is detected..!')
        var='1'
        ser1.write(bytes(var.encode('ascii')))
        time.sleep(0.2)
        var='0'
        
    cv2.imshow('img',img)
    ser1.write(bytes(var.encode('ascii')))
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
