#https://www.youtube.com/watch?v=-bGQNF303QY&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=15
#AI for Everyone LESSON 9: HOMEWORK SOLUTION Understanding ROI in OpenCV

import cv2
import time
#import mediapipe as mp
print(cv2.__version__)

width=640
height=360
snipW=120
snipH=60
# initial position
boxCR=int(height/2)
boxCC=int(width/2)

deltaRow=1
deltaColumn=1

cam=cv2.VideoCapture(0)
print("capture.set = " + str(cam))
while True:

    _,frame=cam.read()
    frameROI=frame[int(boxCR-snipH/2):int(boxCR+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCR-snipH/2):int(boxCR+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]=frameROI

    if boxCR-snipH/2<=0 or boxCR+snipH/2>=height:
        deltaRow=deltaRow*(-1)
    if boxCC-snipW/2<=0 or boxCC+snipW/2>=width:
        deltaColumn=deltaColumn*(-1)


    boxCR=boxCR+deltaRow
    boxCC=boxCC+deltaColumn

    cv2.imshow("my ROI",frameROI)
    cv2.moveWindow('my ROI',width, 0)
    cv2.imshow("my WEBcam",frame)
    cv2.moveWindow('color',0,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()