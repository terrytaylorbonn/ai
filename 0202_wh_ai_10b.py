#https://www.youtube.com/watch?v=QsHFRvRmTAw&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=17
#AI for Everyone LESSON 10: HOMEWORK SOLUTION Create a Region of Interest with the Mouse

import cv2
import time
#import mediapipe as mp
print(cv2.__version__)
evt=0
def mouseClick(event,xPos,yPos,flags,params):
    global pnt1
    global pnt2
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse event was ', event)    
#        print('at position ', xPos, yPos)  
        pnt1=(xPos,yPos)
        evt=event  
    if event==cv2.EVENT_LBUTTONUP:
        print('mouse event was ', event)    
#        print('at position ', xPos, yPos)  
        pnt2=(xPos,yPos)
        evt=event  
    if event==cv2.EVENT_RBUTTONUP:
        print('mouse event was ', event)    
#        print('at position ', xPos, yPos)  
        evt=event  

width=640
height=360

cam=cv2.VideoCapture(0)
print("capture.set = " + str(cam))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',mouseClick)

while True:

    _,frame=cam.read()

    if evt==4:
       cv2.rectangle(frame, pnt1, pnt2, (0,0,250),2)
       ROI=frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
       cv2.imshow("ROI",ROI)
       cv2.moveWindow('ROI',int(width*1.1),0)

    cv2.imshow("my WEBcam",frame)
    cv2.moveWindow('cqolor',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()