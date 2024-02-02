#0128_cmd_camera.py 13:50

from pymavlink import mavutil
from pymavlink import mavwp
import time

# Create the connection
# From topside computer

#connection = mavutil.mavlink_connection('tcp:192.168.1.204:5763')
#connection = mavutil.mavlink_connection('tcp:localhost:5763')
#connection = mavutil.mavlink_connection('udpin:localhost:14551')
#connection = mavutil.mavlink_connection('udpin:localhost:14445')
connection = mavutil.mavlink_connection('udpin:localhost:14551')

print("0 heartbeat")
#connection.wait_heartbeat()

while True:
    try:
#        msg = connection.recv_match(type = ['SYSTEM_TIME'],blocking = True)
#        msg = connection.recv_match(type = ['Reached command'],blocking = True)
#        msg = connection.mav(type = ['MAV_CMD_DO_SET_MODE'],blocking = True)
#        msg = connection.recv_match(type = ['DO_SET_CAM_TRIGG_DIST'],blocking = True)
   #     msg = connection.recv_match(type = ['MAV_CMD_NAV_WAYPOINT'],blocking = True)
#        msg = connection.recv_match(type = ['241'],blocking = True)
 #       msg = connection.mav(type = ['system_time_send'],blocking = True)
 #       msg = connection.mavlink.mavlink_message_id(type = ['SYS_STATUS'],blocking = True)
        msg = connection.mavlink(mavlink_message_id = ['SYS_STATUS'],blocking = True)
        print(msg.to_dict())
        

#        print(connection.recv_match().to_dict())
#        print(connection.mav().to_dict())
#         print(connection)
    except:
        print("EXCEPTION=========================")       
#        pass
    time.sleep(0.1)


# while True:
#     if input('Press 1 for M') == '1':
#         break

# connection.mav.command_long_send(
#         connection.target_system, connection.target_component,
#         mavutil.mavlink.MAV_CMD_REQUEST_CAMERA_INFORMATION,
#         1, # set position
#         0, # param1
#         0, # param21
#         0, # param3
#         0, # param4
#         -35.36326388, # lat
#         149.16524413, # lon
#         0) 

# connection.mav.command_long_send(
#         connection.target_system, connection.target_component,
#         mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
#         0, # set position
#    k     259, # set position
#         0, # param1
#         0, # param21
#         0, # param3
#         0, # param4
#         0, # lat
#         0) 

connection.mav.command_long_send(
        connection.target_system, connection.target_component,
        mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,
        0, # set position
        206, # set position
        0, # param1
        0, # param21
        0, # param3
        0, # param4
        0, # lat
        0) 

print("1b")
#msg = connection.recv_match(type = ['MAV_CMD_DO_SET_CAM_TRIGG_DIST'],blocking = True)
msg = connection.recv_match(type = 206,blocking = True)
print(msg.result)
# msg = connection.recv_match(type = 259,blocking = True)
print("1c")
# time.sleep(1)

# print("2")

# # while True:
# #     if input('Press 2 for mavlink.MAVLink_mission_clear_all_message .. no s') == '2':
# #         break

# connection.mav.send(ma1vutil.mavlink.MAVLink_mission_clear_all_message( 
#             connection.target_system,
#             connection.target_component))

# print("3")

# # while True:
# #     if input('Press 3 for mavlink.MAVLink_mission_count_message .. no s') == '3':
# #         break

# connection.mav.send(mavutil.mavlink.MAVLink_mission_count_message( 
#             connection.target_system,
#             connection.target_component,
#             3,  # 3 waypoints
#             0))

# print("3b")

# msg = connection.recv_match(type=['MISSION_REQUEST'],blocking=True)

# print("5")

# # while True:
# #     if input('Press 5 for mavutil.mavlink.MAV_CMD_NAV_TAKEOFF') == '5':
# #         break

# #Click: -35.36325923 149.16524527

# connection.mav.send(mavutil.mavlink.MAVLink_mission_item_message(
#         connection.target_system,                       # Target system ID
#         connection.target_component,                    # Target component ID
#         0,                                              # 1 sequence
#         3,                                              # 2 relative MAV_FRAME (0 for first, 3 for all others) 
#         mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,            # 3     22
#         1,                                              # 1 current (1 for first, 0 for all others)
#         1,                                              # autocontinue Autocontinue to next waypoint. 0: false, 1: true. 
#                                                         #     11 strip?? Set false to pause mission after the item completes.

#         0.0,                                            # 4 param1
#         0.0,                                            # 5 param2
#         0.0,                                            # 6 param3
#         0.0,                                            # 7 param4

#         0.0,                                            # 8 x param5 (FLOAT AS ALL OTHERS)
#         0.0,                                            # 9 y param6 
#         10.0,                                           # 10 zparam7
#         0))                                             # mav mission type


# print("5b")

# msg = connection.recv_match(type=['MISSION_REQUEST'],blocking=True)


# print("4")

# # while True:
# #     if input('Press 4 for mavutil.mavlink.MAV_CMD_NAV_WAYPOINT') == '4':
# #         break

# connection.mav.send(mavutil.mavlink.MAVLink_mission_item_message(
#         connection.target_system,                       # Target system ID
#         connection.target_component,                    # Target component ID
#         1,                                              # 0 sequence
#         3,                                              # 2 relative MAV_FRAME (0 for first, 3 for all others) 
#         mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,            # 3     22
#         0,                                              # 1 current (1 for first, 0 for all others)
#         1,                                              # autocontinue Autocontinue to next waypoint. 0: false, 1: true. 
#                                                         #     11 strip?? Set false to pause mission after the item completes.

#         0.0,                                            # 4 param1
#         0.0,                                            # 5 param2
#         0.0,                                            # 6 param3
#         0.0,                                            # 7 param4
#         -35.3620,                                    # 8 x param5 (FLOAT AS ALL OTHERS)
#         149.1652,                                    # 9 y param6 
#         15.0,                                           # 10 zparam7
#         0))                                             # mav mission type ??? int(float(linearray[11].strip())

# print("4b")

# msg = connection.recv_match(type=['MISSION_REQUEST'],blocking=True)


# print("6")

# # while True:
# #     if input('Press 6 for mavutil.mavlink.MAV_CMD_NAV_WAYPOINT') == '6':
# #         break

# connection.mav.send(mavutil.mavlink.MAVLink_mission_item_message(
#         connection.target_system,                       # Target system ID
#         connection.target_component,                    # Target component ID
#         2,                                              # 0 sequence
#         3,                                              # 2 relative MAV_FRAME (0 for first, 3 for all others) 
#         mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,          # 3     22
#         0,                                              # v2=0  1 current (1 for first, 0 for all others)
#         0,                                              # autocontinue Autocontinue to next waypoint. 0: false, 1: true. 
#                                                         #     11 strip?? Set false to pause mission after item completes.

#         0.0,                                            # 4 param1
#         0.0,                                            # 5 param2
#         0.0,                                            # 6 param3
#         0.0,                                            # 7 param4

#         -35.3620,                                   # 8 x param5 (FLOAT AS ALL OTHERS)
#         149.1662,                                   # 9 y param6 
#         20.0,                                           # 10 zparam7
#         0))                                             # mav mission type

# # this never arrives
# #msg = connection.recv_match(type=['MISSION_REQUEST'],blocking=True)


# print("DONE v2 ==================")