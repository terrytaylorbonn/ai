
import cv2
print(cv2.__version__)
#dispW=1280
#dispH=960
flip=2

#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
print("1")
cam=cv2.VideoCapture(4)  
print("2")


#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
 
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        print("3")
        break
cam.release()
cv2.destroyAllWindows()