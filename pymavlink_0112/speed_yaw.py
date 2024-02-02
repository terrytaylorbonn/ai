#23.0112
from pymavlink import mavutil

# Start a connection listening on a UDP port
the_connection = mavutil.mavlink_connection('udpin:localhost:14551') #TERRY

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % 
   (the_connection.target_system, the_connection.target_component))

# Once connected, use 'the_connection' to get and send messages

# the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
#         mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, 45, 25, -1, 1, 0, 0, 0 )

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
        mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED, 0, 0, 1, 0, 0, 0, 0, 0 )

#https://mavlink.io/en/messages/common.html#MAV_CMD_DO_CHANGE_SPEED
# MAV_CMD_DO_CHANGE_SPEED (178 )
# [Command] Change speed and/or throttle set points. The value persists until it is overridden or there is a mode change
# Param (:Label)	Description	Values	Units
# 1: Speed Type	Speed type of value set in param2 (such as airspeed, ground speed, and so on)	SPEED_TYPE	
# (1) 2: Speed	Speed (-1 indicates no change, -2 indicates return to default vehicle speed)	min: -2	m/s
# 3: Throttle	Throttle (-1 indicates no change, -2 indicates return to default vehicle throttle value)	min: -2	%
# 4	Reserved (set to 0)		
# 5	Reserved (set to 0)		
# 6	Reserved (set to 0)		
# 7	Reserved (set to 0)