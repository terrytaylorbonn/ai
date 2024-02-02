#https://www.youtube.com/watch?v=gD_HWj_hvbo&list=PLGs0VKk2DiYzguDvh5xk2XoX9V1VKP5Hv&index=28&t=1327s

import cv2
import mediapipe as mp

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

print(cv2.__version__)
myCam=cv2.VideoCapture(0)
while True:
    _,frame=myCam.read()
    grayFrame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",grayFrame)
    cv2.moveWindow('gray',0,0)
    cv2.imshow("color",frame)
    cv2.moveWindow('color',640,0)
    cv2.imshow("gray2",grayFrame)
    cv2.moveWindow('gray2',640,480)
    cv2.imshow("color2",frame)
    cv2.moveWindow('color2',0,480)
    if cv2.waitKey(1)==ord('q'):
        break
myCam.release()