import cv2
import paho.mqtt.client as mqtt
import numpy as np
from time import sleep
cap=cv2.VideoCapture(0)
TrDict={'csrt':cv2.TrackerCSRT_create}
tracker=TrDict['csrt']()
ret,frame=cap.read()

frame=cv2.resize(frame,(640,480))
bb=cv2.selectROI(frame)
tracker.init(frame,bb)


count=0



    
def track(img):
    
    success,box=tracker.update(img)
    if success:
        (x,y,w,h)=[int(a)for a in box]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cx = (x + x + w) // 2
        cy = (y + y + h) // 2
        cv2.circle(img,(cx,cy),5,(0,0,255),-1)

       

       

    

  
while True:
    ret,frame=cap.read()
    count += 1
    if count % 10 != 0:
        continue
    frame=cv2.resize(frame,(640,480))

    track(frame)

           
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()

cv2.destroyAllWindows()
