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
start_point = (0, 0)
end_point = (0, 0)
start_point1 = (0, 0)
end_point1 = (0, 0)
color = (0, 255, 0)
thickness = 2

count=0

def forward():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("forward",'utf-8')))     



def stop():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("stop",'utf-8')))     

def back():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("back",'utf-8')))     


    
def track(img):
    
    success,box=tracker.update(img)
    if success:
        (x,y,w,h)=[int(a)for a in box]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cx = (x + x + w) // 2
        cy = (y + y + h) // 2
        cv2.circle(img,(cx,cy),5,(0,0,255),-1)

        print(cx)

       

    

  
while True:
    ret,frame=cap.read()
    count += 1
    if count % 10 != 0:
        continue
    frame=cv2.resize(frame,(640,480))
 #   cv2.line(frame, start_point, end_point, color, thickness)
 #   cv2.line(frame, start_point1, end_point1, color, thickness)
    track(frame)

           
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
stop()
cv2.destroyAllWindows()
