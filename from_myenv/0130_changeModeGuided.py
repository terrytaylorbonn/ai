
# ubuntu Downloads/my_env/0130_changeModeGuide.py
#   nano = 202
#   ubuntu = 204
#   output add ...203:14551
#   win11 104

from pymavlink import mavutil

# 0 CONNECTION ==============================================================

#connection = mavutil.mavlink_connection('udpin:192.168.1.202:14551')
#connection = mavutil.mavlink_connection('udpin:localhost:14551')
connection = mavutil.mavlink_connection('tcp:localhost:5763')
#connection = mavutil.mavudp('localhost:14551', input=True, source_system=255, source_component=0, use_native=False, timeout=0)
#connection = mavutil.mavlink_connection('udpin:localhost:14551')
#print(dir(connection.mav))

print("0 connection = " + str(connection))

#print(dir(connection.mav))



# # 1 ARM / TAKEOFF ==============================================================

# while True:
#     # some code here
#     if input('Press 1 to arm/takeoff') == '1':
#         break

# message = connection.mav.command_long_encode(
#          connection.target_system,                       # Target system ID
#          connection.target_component,                    # Target component ID
#          mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,               # ID of command to send
#          0,                                              # 
#          #-----------------------------------------------------------------
#          1,    #                                          # param1 
#          0, #21196 force arm                                # param2 
#          0,                                              # param3
#          0,                                              # param4
#          0,                                              # param5
#          0,                                              # param6
#          0)                                              # param7
# print("1b") 
# connection.mav.send(message)
# print("1c")

# message = connection.mav.command_long_encode(
#          connection.target_system,                       # Target system ID
#          connection.target_component,                    # Target component ID
#          mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,               # ID of command to send
#          0,                                              # 
#          #-----------------------------------------------------------------
#          0,    #                                          # param1 
#          0,                            # param2 
#          0,                                              # param3
#          0,                                              # param4
#          0,                                              # param5
#          0,                                              # param6
#          11)                                              # param7
# print("1d")  
# connection.mav.send(message)
# print("1e")

# # 2 AUTO ==============================================================

# while True:
#     # some code here
#     if input('Press 2 to -> auto') == '2':
#         break

# message = connection.mav.command_long_encode(
#          connection.target_system,                       # Target system ID
#          connection.target_component,                    # Target component ID
#          mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
#          0,                                              # 
#          #-----------------------------------------------------------------
#          1,    # 1 = flight mode 1 ?                                         # param1 
#          3,       # 1=acro  3 = auto?                                   # param2 
#          0,                                              # param3
#          0,                                              # param4
#          0,                                              # param5
#          0,                                              # param6
#          0)                                              # param7
# print("2b")    
# connection.mav.send(message)
# print("2c")

# 3 GUIDED ==============================================================

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

# 4 NED ==============================================================

# while True:
#     # some code here
#     if input('Press 4 to -> NED 20m') == '4':
#         break

# connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, 
#             connection.target_system,
#             connection.target_component, 
#             mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(0b110111111000), 
#             20, 0, -10, 0, 0, 0, 0, 0, 0, 0, 0))

# print("4c")
 
# 5 AUTO ==============================================================

# while True:
#     # some code here
#     if input('Press 5 to -> AUTO') == '5':
#         break

message = connection.mav.command_long_encode(
         connection.target_system,                       # Target system ID
         connection.target_component,                    # Target component ID
         mavutil.mavlink.MAV_CMD_DO_SET_MODE,               # ID of command to send
         0,                                              # 
         #-----------------------------------------------------------------
         1,    # 1 = flight mode 1 ?                                         # param1 
         3,       # 1=acro  3 = auto?  6 = rtl?                                  # param2 
         0,                                              # param3
         0,                                              # param4
         0,                                              # param5
         0,                                              # param6
         0)                                              # param7
print("5b")
connection.mav.send(message)
print("5c")

# 6 RTL ==============================================================

while True:
    # some code here
    if input('Press 6 to -> RTL') == '6':
        break

# HAD TO RUN TWICE TO GET RTL TO WORK

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
print("6b")
connection.mav.send(message)
print("6c")

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
print("6b")
connection.mav.send(message)
print("6c")

# ==============================================================
 
"""
#response = connection.recv_match(type='HEARTBEAT', blocking=True)
#response = connection.recv_match(type='SYS_STATUS', blocking=True)
response = connection.recv_match(type='MAV_CMD_DO_JUMP',blocking=True)
print("6 AUTO_PILOT_VERSION")
if response:
 #   print("Command response")
#    print("response.type = ", response.type)
    print("response = ", response)
#    print("response.command ()                      = " + str(response.command))
#    print("response.result  (0=MAV_RESULT_ACCEPTED) = " + str(response.result)) 
else:
    print("no response")
print("7")
"""

