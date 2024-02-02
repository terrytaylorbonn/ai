
import cv2
print(cv2.__version__)
from pymavlink import mavutil

def haar(cam):
  
    while True:
        flagg = 0 
        ret, frame = cam.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces = list of arrays, upper corner of face, etc.....
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
            print("detected... ")
            flagg = 1
            return(flagg)
        cv2.imshow('nanoCam',frame)
        cv2.moveWindow('nanoCam', 0, 0)
        # if cv2.waitKey(1)==ord('q'):
        #     flagg = 2 
        #     return(flagg)

dispW=640
dispH=480
flip=2

connection = mavutil.mavlink_connection('tcp:localhost:5763')
print("0 connection = " + str(connection))

cam=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('/home/tt15/Downloads/face.xml')
cc_control=0
print("cc_control = " + str(cc_control))

while True:

    flagg=haar(cam)

    if (cc_control==0 & flagg==1):

        # 3 GUIDED ==============================================================

        # while True:
        #     # some code here
        #     if input('Press 3 to -> guided') == '3':
        #         break

         message = connection.mav.command_long_encode(
                  connection.target_system,                       # Target system ID
                  connection.target_component,                    # Target component ID
                  mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
                  0,                                              # 
                  #-----------------------------------------------------------------
                  1,    # 1 = flight mode 1 ?                                         # param1 
                  4,       # 1=acro  3 = auto?    4=guided??                               # param2 
                  0,                                              # param3
                  0,                                              # param4
                  0,                                              # param5
                  0,                                              # param6
                  0)                                              # param7
         print("3b")
         connection.mav.send(message)
         print("3c")
         message = connection.mav.command_long_encode(
                  connection.target_system,                       # Target system ID
                 connection.target_component,                    # Target component ID
                  mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
                  0,                                              # 
                 #-----------------------------------------------------------------
                  1,    # 1 = flight mode 1 ?                                         # param1 
                  4,       # 1=acro  3 = auto?    4=guided??                               # param2 
                  0,                                              # param3
                  0,                                              # param4
                  0,                                              # param5
                  0,                                              # param6
                  0)                                              # param7
         print("3b")
         connection.mav.send(message)
         print("3c")

        # 4 NED ==============================================================

        # while True:
        #     # some code here
        #     if input('Press 4 to -> NED 20m') == '4':
        #         break

         connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, 
                    connection.target_system,
                    connection.target_component, 
                    mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(0b110111111000), 
                    20, 0, -10, 0, 0, 0, 0, 0, 0, 0, 0))

         cc_control=1
         print("cc_control = " + str(cc_control))

    if (cc_control==1 & cv2.waitKey(1)==ord('q')):
           cam.release()
           cv2.destroyAllWindows()
           break

    print("4c")





 




