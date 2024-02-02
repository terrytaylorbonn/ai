
# ubuntu Downloads/my_env/OpenCV-Tutorials 0131_haar_v6.py
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


while True:
    # some code here
    if input('Put copter into guided moded and press g') == 'g':
        break


# 1 ARM / TAKEOFF ==============================================================

while True:
    # some code here
    if input('Press 1 to arm/takeoff X2') == '1':
        break

message = connection.mav.command_long_encode(
         connection.target_system,                       # Target system ID
         connection.target_component,                    # Target component ID
         mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,               # ID of command to send
         0,                                              # 
         #-----------------------------------------------------------------
         1,    #                                          # param1 
         0, #21196 force arm                                # param2 
         0,                                              # param3
         0,                                              # param4
         0,                                              # param5
         0,                                              # param6
         0)                                              # param7
print("1b") 
connection.mav.send(message)
print("1c")

message = connection.mav.command_long_encode(
         connection.target_system,                       # Target system ID
         connection.target_component,                    # Target component ID
         mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,               # ID of command to send
         0,                                              # 
         #-----------------------------------------------------------------
         0,    #                                          # param1 
         0,                            # param2 
         0,                                              # param3
         0,                                              # param4
         0,                                              # param5
         0,                                              # param6
         11)                                              # param7
print("1d")  
connection.mav.send(message)
print("1e")

# 2 AUTO ==============================================================

while True:
    # some code here
    if input('Press 2 to -> auto') == '2':
        break

message = connection.mav.command_long_encode(
         connection.target_system,                       # Target system ID
         connection.target_component,                    # Target component ID
         mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
         0,                                              # 
         #-----------------------------------------------------------------
         1,    # 1 = flight mode 1 ?                                         # param1 
         3,       # 1=acro  3 = auto?                                   # param2 
         0,                                              # param3
         0,                                              # param4
         0,                                              # param5
         0,                                              # param6
         0)                                              # param7
print("2b")    
connection.mav.send(message)
print("2c")

# # 3 GUIDED ==============================================================

# while True:
#     # some code here
#     if input('Press 3 to -> guided') == '3':
#         break

# message = connection.mav.command_long_encode(
#          connection.target_system,                       # Target system ID
#          connection.target_component,                    # Target component ID
#          mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
#          0,                                              # 
#          #-----------------------------------------------------------------
#          1,    # 1 = flight mode 1 ?                                         # param1 
#          4,       # 1=acro  3 = auto?    4=guided??                               # param2 
#          0,                                              # param3
#          0,                                              # param4
#          0,                                              # param5
#          0,                                              # param6
#          0)                                              # param7
# print("3b")
# connection.mav.send(message)
# print("3c")

while True:
    # some code here
    if input('Press a to to start ai ') == 'a':
        break


cam=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('/home/tt15/Downloads/face.xml')
cc_control=0
print("cc_control = " + str(cc_control))

while True:

    flagg=haar(cam)

    if (flagg==1):

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

        #  cc_control=1
        #  print("cc_control = " + str(cc_control))
         break

print("4c")


while True:
    # some code here
    if input('Press r to to rtl') == 'r':
        break


#===== 3 ===============================================================
message = connection.mav.command_long_encode(
         connection.target_system,                       # Target system ID
         connection.target_component,                    # Target component ID
         mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
         0,                                              # 
         #-----------------------------------------------------------------
         1,    # 1 = flight mode 1 ?                                         # param1 
         6,       # 1=acro  3 = auto?  6 = rtl?                                  # param2 
         0,                                              # param3
         0,                                              # param4
         0,                                              # param5
         0,                                              # param6
         0)                                              # param7
print("4modeeeeeeeeee")
# Send COMMAND_INT     
connection.mav.send(message)
print("5modeeeeeeeee")



while True:
    # some code here
    if input('Press l (small L ) to land') == 'l':
        break


# 2 COMMAND ---------------------------------------------------------------------------
# Define command_long_encode message that contains 
#    command         21 MAV_CMD_NAV_LAND 
#    command message    (none) 
message = connection.mav.command_long_encode(
        connection.target_system,                       # Target system ID
        connection.target_component,                    # Target component ID
        mavutil.mavlink.MAV_CMD_NAV_LAND,               # ID of command to send
        0,                                              # 
        #-----------------------------------------------------------------
        0,                                              # param1 
        0,                                              # param2 
        0,                                              # param3
        0,                                              # param4
        0,                                              # param5
        0,                                              # param6
        0)                                              # param7
print("4")
# Send COMMAND_INT     
connection.mav.send(message)
print("5")

# 3 RESPONSE ----------------------------------------------------------------------------
# Wait for response (blocking) to command / print result
response = connection.recv_match(type='COMMAND_ACK', blocking=True)
print("6")
if response:
    print("Command accepted")
    print("response.command ()                      = " + str(response.command))
    print("response.result  (0=MAV_RESULT_ACCEPTED) = " + str(response.result)) 
else:
    print("no response")
print("7")


while True:

    if (cv2.waitKey(1)==ord('q')):
           cam.release()
           cv2.destroyAllWindows()
           break






 




