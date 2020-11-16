#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from sensor_msgs.msg import LaserScan
#global coordinates of robot
x = 0.0
y = 0.0 
theta = 0.0

def callback(dt):

  
    thr1 = 0.8 # Laser scan range threshold
    thr2 = 0.8
    if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2: # Checks if there are obstacles in front and
                                                                         # 15 degrees left and right (Try changing the
		# the angle values as well as the thresholds)
        speed.linear.x = 0.5 # go forward (linear velocity)
        speed.angular.z = 0.0 # do not rotate (angular velocity)
    else:
        speed.linear.x = 0.0 # stop
        speed.angular.z = 0.3 # rotate counter-clockwise
        if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
    pub.publish(speed) # publish the move object
    r.sleep()


def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    #get the theta value from orientation
    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    
rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
sub = rospy.Subscriber("/scan", LaserScan, callback)
speed = Twist()

r = rospy.Rate(4)

#goal position
goal = Point()
goal.x = 7
goal.y = 7

while not rospy.is_shutdown():
    #difference of the goal and current position of the robot and can get orientation
    inc_x = goal.x -x
    inc_y = goal.y -y

    angle_to_goal = atan2(inc_y, inc_x)
   
    if abs(angle_to_goal - theta) > 0.1 :
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0
    
    pub.publish(speed)
    r.sleep() 