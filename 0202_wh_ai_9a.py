#https://www.youtube.com/watch?v=E46B7NPWK38&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=14

import cv2
import time
#import mediapipe as mp
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0)
print("capture.set = " + str(cam))
tLast=time.time()
time.sleep(.1)
while True:

    _,frame=cam.read()

    frameROI=frame[150:210,250:390]
    frameROIGray=cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIBGR=cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)

    cv2.imshow('my BGR ROI', frameROIBGR)
    cv2.moveWindow('my BGRROI', 650,180)

    frame[150:210,250:390]=frameROIBGR
    
    cv2.imshow('my gray ROI', frameROIBGR)
    cv2.moveWindow('my ROI', 650,90)
    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI', 650,0)

    # frame[140:220,250:390]=(0,0,255)
    # cv2.rectangle(frame,(250,140),(390,220),(0,255,0),4)
    cv2.imshow("color",frame)
    cv2.moveWindow('color',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()