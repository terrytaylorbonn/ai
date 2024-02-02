
# 24.0117 08:30 
# Example: Set that a message is streamed at particular rate
#   nano = 192.168.1.203  202
#   ubuntu = 192.168.1.204
#   >output add 192.168.1.203:14551


from pymavlink import mavutil

print("1")

# 1 CONNECTION ---------------------------------------------------------------------------
#connection = mavutil.mavlink_connection('udpin:192.168.1.202:14551')
connection = mavutil.mavlink_connection('udpin:localhost:14551')

#connection = mavutil.mavudp('localhost:14551', input=True, source_system=255, source_component=0, use_native=False, timeout=0)

print("2 the connection = " + str(connection))




# 2 COMMAND ---------------------------------------------------------------------------
# Define command_long_encode message that contains 
#    command         21 MAV_CMD_NAV_LAND 
#    command message    (none) 
message = connection.mav.command_long_encode(
        connection.target_system,                       # Target system ID
        connection.target_component,                    # Target component ID
        mavutil.mavlink.MISSION_REQUEST_LIST,               # ID of command to send
        0,                                              # 
        #-----------------------------------------------------------------
        148, # AUTO_PILOT_VERSION,                                              # param1 
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


#response = connection.recv_match(type='HEARTBEAT', blocking=True)
#response = connection.recv_match(type='SYS_STATUS', blocking=True)
response = connection.recv_match(type=148)
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



# # 2 COMMAND ---------------------------------------------------------------------------
# # Define command_long_encode message that contains 
# #    command         21 MAV_CMD_NAV_LAND 
# #    command message    (none) 
# message = connection.mav.command_long_encode(
#         connection.target_system,                       # Target system ID
#         connection.target_component,                    # Target component ID
#         mavutil.mavlink.MAV_CMD_NAV_LAND,               # ID of command to send
#         0,                                              # 
#         #-----------------------------------------------------------------
#         0,                                              # param1 
#         0,                                              # param2 
#         0,                                              # param3
#         0,                                              # param4
#         0,                                              # param5
#         0,                                              # param6
#         0)                                              # param7
# print("4")
# # Send COMMAND_INT     
# connection.mav.send(message)
# print("5")

# # 3 RESPONSE ----------------------------------------------------------------------------
# # Wait for response (blocking) to command / print result
# response = connection.recv_match(type='COMMAND_ACK', blocking=True)
# print("6")
# if response:
#     print("Command accepted")
#     print("response.command ()                      = " + str(response.command))
#     print("response.result  (0=MAV_RESULT_ACCEPTED) = " + str(response.result)) 
# else:
#     print("no response")
# print("7")

