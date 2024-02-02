import cv2 
print(cv2.__version__)
dispW=640
dispH=480
flip=2
print("1")
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1280, height=720, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#print("2")
#cam=cv2.VideoCapture(camSet)   #pi cam
cam=cv2.VideoCapture(0)    #logi webcam usb
#print("3")
while True:
#   ret, frame=cam.read()
   frame=cv2.imread('smarties.png')
   cv2.imshow('nanoCam', frame)
   cv2.moveWindow('nanoCam',0,0)
   if cv2.waitKey(1)==ord('q'):
      print("4")
      break
cam.release()
cv2.destroyAllWindows()

print("end")