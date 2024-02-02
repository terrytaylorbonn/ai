#https://www.youtube.com/watch?v=gD_HWj_hvbo&list=PLGs0VKk2DiYzguDvh5xk2XoX9V1VKP5Hv&index=28&t=1327s

import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
FDetect = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

mp_drawing=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    _,image=cap.read()
    results=FDetect.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)) 
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)

    cv2.imshow("mediapipe face detect ",image)
    cv2.moveWindow('mp face dtect',0,0)
    if cv2.waitKey(5) &0xFF==ord('q'):
        break

# myCam=cv2.VideoCapture(0)
# while True:
#     _,frame=myCam.read()
#     cv2.imshow("xxx",frame)
#     cv2.moveWindow('xxxx',0,0)
#     if cv2.waitKey(1)==ord('q'):
#         break
# myCam.release()