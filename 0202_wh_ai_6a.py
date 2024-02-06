#https://www.youtube.com/watch?v=bJIzOniUaAw&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=8

# mp_face_detection = mp.solutions.face_detection
# FDetect = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

# mp_drawing=mp.solutions.drawing_utils
# cap=cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)

# while True:
#     _,image=cap.read()
#     results=FDetect.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)) 
#     if results.detections:
#         for detection in results.detections:
#             mp_drawing.draw_detection(image, detection)

#     cv2.imshow("mediapipe face detect ",image)
#     cv2.moveWindow('mp face dtect',0,0)
#     if cv2.waitKey(5) &0xFF==ord('q'):
#         break

import cv2
#import mediapipe as mp

print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0)
#cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)

#https://stackoverflow.com/questions/69558539/cv2-videocapture0-cv2-dshow-returns-none
#DSHOW (and MSMF) are windows only.
#on linux, use V4L, FFMPEG or GSTREAMER
#also, please check the return val of capture.set(), not all properties/values will be supported on any given machine
print("capture.set = " + str(cam))

#cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
#cam.set(cv2.CAP_PROP_FPS,30)
#cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    _,frame=cam.read()
 #   grayFrame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 #   cv2.imshow("gray",grayFrame)
#    cv2.moveWindow('gray',0,0)
    cv2.imshow("color",frame)
    cv2.moveWindow('color',0,0)
#    cv2.imshow("gray2",grayFrame)
#    cv2.moveWindow('gray2',640,480)
##    cv2.imshow("color2",frame)
 #   cv2.moveWindow('color2',0,480)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()