#https://www.youtube.com/watch?v=HmuGQ-XFPgc&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=16#AI 
#AI for Everyone LESSON 10: Processing Mouse Clicks and Events in OpenCV

import cv2
import time
#import mediapipe as mp
print(cv2.__version__)
evt=0
def mouseClick(event,xPos,yPos,flags,params):
    global evt,pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse event was ', event)    
        print('at position ', xPos, yPos)  
        pnt=(xPos,yPos)
        evt=event  
    if event==cv2.EVENT_LBUTTONUP:
        print('mouse event was ', event)    
        print('at position ', xPos, yPos)    
        evt=event  
    if event==cv2.EVENT_RBUTTONUP:
        print('right button up ', event)    
        pnt=(xPos,yPos)
        evt=event  

width=640
height=360

cam=cv2.VideoCapture(0)
print("capture.set = " + str(cam))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',mouseClick)

while True:

    _,frame=cam.read()

    if evt==1 or evt==4:
       cv2.circle(frame, pnt,25, (255,0,0),2)

    cv2.imshow("my WEBcam",frame)

    cv2.moveWindow('color',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()