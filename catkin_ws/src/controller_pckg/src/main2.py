#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from sensor_msgs.msg import LaserScan
from math import radians

class DrawCircle():
     
    def __init__(self):
        global pub

        self.pub= rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber("/scan", LaserScan,self.collison)
        self.subodo = rospy.Subscriber("/odom", Odometry,self.newOdom)
        self.r = rospy.Rate(20); #Frequency
        
        
        
    def collison(self,dt):
        thr1 = 1 # Laser scan range threshold
        thr2 = 1
        speed=Twist()

        if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2: 
            speed.linear.x = 0.3 
            speed.angular.z = 0.0 
        else:
            speed.linear.x = 0.0 
            speed.angular.z = 0.5
            if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2:
                speed.linear.x = 0.5
                speed.angular.z = 0.0

        self.pub.publish(speed)
        self.r.sleep()        

    def newOdom(self,msg):
        global x
        global y
        global theta

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
            #get the theta value from orientation
        #SPEED & ANGLE ADJUSTMENT
        move = Twist()
        a = 10 #angle
        move.angular.z = radians(a); #angula
        move.linear.x = 0.3 #linear
        for x in range(0,(360/a)):
            self.pub.publish(move)
            self.r.sleep()

if __name__ == '__main__':
    rospy.init_node('drawcircle', anonymous=False) 
    hm1=DrawCircle()

    while not rospy.is_shutdown(): 
        rospy.loginfo("Circling")
        hm1.collison()
             
