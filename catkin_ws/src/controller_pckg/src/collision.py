#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist #

def callback(dt):
    print '-------------------------------------------'
    print 'Range data at 0 deg:   {}'.format(dt.ranges[0])
    print 'Range data at 15 deg:  {}'.format(dt.ranges[15])
    print 'Range data at 345 deg: {}'.format(dt.ranges[345])
    print '-------------------------------------------'
    thr1 = 0.8 # Laser scan range threshold
    thr2 = 0.8
    
    move.linear.x = 0.5 #linear velocity
    move.angular.z = 0.1 #angular velocity
    
    pub.publish(move) # publish the move object


move = Twist() # Creates a Twist message type object
rospy.init_node('obstacle_avoidance_node') # Initializes a node
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  # Publisher object which will publish "Twist" type messages
                            				 # on the "/cmd_vel" Topic, "queue_size" is the size of the
                                                         # outgoing message queue used for asynchronous publishing

sub = rospy.Subscriber("/scan", LaserScan, callback)  # Subscriber object which will listen "LaserScan" type messages
                                                      # from the "/scan" Topic and call the "callback" function
						      # each time it reads something from the Topic

rospy.spin() # Loops infinitely until someone stops the program execution
