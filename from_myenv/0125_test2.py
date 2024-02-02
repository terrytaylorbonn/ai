
# 24.0117 08:30 
# Example: Set that a message is streamed at particular rate
#   nano = 192.168.1.203  202
#   ubuntu = 192.168.1.204
#   >output add 192.168.1.203:14551


from pymavlink import mavutil

print("1")

# 1 CONNECTION ---------------------------------------------------------------------------
#connection = mavutil.mavlink_connection('udpin:192.168.1.202:14551')
#connection = mavutil.mavlink_connection('udpin:localhost:14551')
#connection = mavutil.mavlink_connection('tcp:localhost:5760')
connection = mavutil.mavudp('localhost:14551', input=True, source_system=255, source_component=0, use_native=False, timeout=0)
print(dir(connection.mav))

print("2 the connection = " + str(connection))


 

print("3a send waypoint 0")

connection.mav.mission_request_int_send(connection.target_system, 
                                    connection.target_component ,0)            
  #                                   0    )            

#print("3b waypoint 0 Message read " + str(connection.recv_match(type="MISSION_COUNT", blocking=True)))

 

#response = connection.recv_match(type='HEARTBEAT', blocking=True)
#response = connection.recv_match(type='SYS_STATUS', blocking=True)
response = connection.recv_match(type=0,blocking=True)
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
