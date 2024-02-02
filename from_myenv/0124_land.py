
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
print("2 the connection = " + str(connection))
# get remote (ubuntu sitl) system/component ids
print(connection.wait_heartbeat())
#connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (connection.target_system, connection.target_component))
print("3")



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

