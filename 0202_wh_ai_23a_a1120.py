#https://toptechboy.com/parsing-mediapipe-for-face-mesh-pose-and-hand-landmarks/
#https://www.youtube.com/watch?v=s09x9rwbnnE&list=PLGs0VKk2DiYyXlbJVaE8y1qr24YldYNDm&index=42
#AI for Everyone LESSON 23 : Parsing Mediapipe Pose, Face Mesh and Hand Landmarks

import cv2
#import time
import mediapipe as mp
print(cv2.__version__)

cam=cv2.VideoCapture(0)
print("capture.set = " + str(cam))

width=1280
height=720
faceMesh=mp.solutions.face_mesh.FaceMesh(False) #, 3, 0.5, 0.5 )
mpDraw=mp.solutions.drawing_utils
font=cv2.FONT_HERSHEY_SIMPLEX
fontSize=.5
fontColor=(0,255,255)
fontThick=1

while True:

    _,frame=cam.read()
#    frame=cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=faceMesh.process(frameRGB)
    print(results.multi_face_landmarks)



    cv2.imshow("my WEBcam",frame)
    cv2.moveWindow('cqolor',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
















# import cv2
# print(cv2.__version__)

# class mpFaceMesh:
#     import mediapipe as mp
#     def __init__(self,still=False,numFaces=3,tol1=.5,tol2=.5,drawMesh=True):
#         self.myFaceMesh=self.mp.solutions.face_mesh.FaceMesh(still,numFaces,tol1,tol2)
#         self.myDraw=self.mp.solutions.drawing_utils
#         self.draw=drawMesh
#     def Marks(self,frame):
#         global width
#         global height
#         drawSpecCircle=self.myDraw.DrawingSpec(thickness=0,circle_radius=0,color=(0,0,255))
#         drawSpecLine=self.myDraw.DrawingSpec(thickness=3,circle_radius=2,color=(255,0,0))
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.myFaceMesh.process(frameRGB)
#         facesMeshLandmarks=[]
#         if results.multi_face_landmarks !=None:
#             for faceMesh in results.multi_face_landmarks:
#                 faceMeshLandmarks=[]
#                 for lm in faceMesh.landmark:
#                     loc=(int(lm.x*width),int(lm.y*height))
#                     faceMeshLandmarks.append(loc)
#                 facesMeshLandmarks.append(faceMeshLandmarks)
#                 if self.draw==True:
#                     self.myDraw.draw_landmarks(frame,faceMesh,self.mp.solutions.face_mesh.FACE_CONNECTIONS,drawSpecCircle,drawSpecLine)
#         return facesMeshLandmarks

# class mpFace:
#     import mediapipe as mp 
#     def __init__(self):
#         self.myFace=self.mp.solutions.face_detection.FaceDetection()
#     def Marks(self,frame):
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.myFace.process(frameRGB)
#         faceBoundBoxs=[]
#         if results.detections != None:
#             for face in results.detections:
#                 bBox=face.location_data.relative_bounding_box
#                 topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
#                 bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
#                 faceBoundBoxs.append((topLeft,bottomRight))
#         return faceBoundBoxs

# class mpPose:
#     import mediapipe as mp
#     def __init__(self,still=False,upperBody=False, smoothData=True, tol1=.5, tol2=.5):
#         self.myPose=self.mp.solutions.pose.Pose(still,upperBody,smoothData,tol1,tol2)
#     def Marks(self,frame):
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.myPose.process(frameRGB)
#         poseLandmarks=[]
#         if results.pose_landmarks:
#             for lm in results.pose_landmarks.landmark:            
#                 poseLandmarks.append((int(lm.x*width),int(lm.y*height)))
#         return poseLandmarks

# class mpHands:
#     import mediapipe as mp
#     def __init__(self,maxHands=2,tol1=.5,tol2=.5):
#         self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
#     def Marks(self,frame):
#         myHands=[]
#         handsType=[]
#         frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         results=self.hands.process(frameRGB)
#         if results.multi_hand_landmarks != None:
#             #print(results.multi_handedness)
#             for hand in results.multi_handedness:
#                 #print(hand)
#                 #print(hand.classification)
#                 #print(hand.classification[0])
#                 handType=hand.classification[0].label
#                 handsType.append(handType)
#             for handLandMarks in results.multi_hand_landmarks:
#                 myHand=[]
#                 for landMark in handLandMarks.landmark:
#                     myHand.append((int(landMark.x*width),int(landMark.y*height)))
#                 myHands.append(myHand)
#         return myHands,handsType

# width=1280
# height=720
# cam=cv2.VideoCapture(3,cv2.CAP_DSHOW)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
# cam.set(cv2.CAP_PROP_FPS, 30)
# cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

# findHands=mpHands(2)
# findFace=mpFace()
# findPose=mpPose()
# findMesh=mpFaceMesh(drawMesh=True)

# font=cv2.FONT_HERSHEY_SIMPLEX
# fontColor=(0,0,255)
# fontSize=.1
# fontThick=1

# cv2.namedWindow('Trackbars')
# cv2.moveWindow('Trackbars',width+50,0)
# cv2.resizeWindow('Trackbars',400,150)


# while True:
#     ignore,  frame = cam.read()
#     frame=cv2.resize(frame,(width,height))
#     handsLM,handsType=findHands.Marks(frame)
#     faceLoc=findFace.Marks(frame)
#     poseLM=findPose.Marks(frame)
#     facesMeshLM=findMesh.Marks(frame)
#     if poseLM != []:
#         for ind in [13,14,15,16]:
#             cv2.circle(frame,poseLM[ind],20,(0,255,0),-1)

#     for face in faceLoc:
#         cv2.rectangle(frame,face[0],face[1],(255,0,0),3)
#     for hand,handType in zip(handsLM,handsType):
#         if handType=='Right':
#             lbl='Right'
#         if handType=='Left':
#             lbl='Left'
#         cv2.putText(frame,lbl,hand[8],font,2,fontColor,2)
#     for faceMeshLM in facesMeshLM:
#         cnt=0
#         for lm in faceMeshLM:
#             cv2.putText(frame,str(cnt),lm,font,fontSize,fontColor,fontThick)
#             cnt=cnt+1

#     cv2.imshow('my WEBcam', frame)
#     cv2.moveWindow('my WEBcam',0,0)
#     if cv2.waitKey(1) & 0xff ==ord('q'):
#         break
# cam.release()