
import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2

##################################---------------------
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

# cam=cv2.VideoCapture(camSet)   #pi cam


#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(0)
print("2")
face_cascade=cv2.CascadeClassifier('/home/tt15/Downloads/face.xml')


while True:
    ret, frame = cam.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #faces = list of arrays, upper corner of face, etc.....
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
