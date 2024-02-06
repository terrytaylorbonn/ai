#https://www.youtube.com/watch?v=97HA3NeYjus&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=12

import cv2
#import mediapipe as mp
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0)
print("capture.set = " + str(cam))
while True:
    _,frame=cam.read()
    frame[140:220,250:390]=(0,0,255)
    cv2.rectangle(frame,(250,140),(390,220),(0,255,0),4)
    cv2.imshow("color",frame)
    cv2.moveWindow('color',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()