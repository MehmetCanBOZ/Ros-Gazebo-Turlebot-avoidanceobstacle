#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from sensor_msgs.msg import LaserScan,Imu
from math import radians


class DrawCircle():
     
    def __init__(self):
        # INITIALIZATION
        global pub
        global move
        #Publisher and Subscriber Topic
        self.pub= rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber("/scan", LaserScan,self.collison)
        self.odo = rospy.Subscriber("/odom", Odometry,self.newOdom)
        self.im=rospy.Subscriber("/imu",Imu,self.speedvalue)
        rate = rospy.Rate(5)  
        self.move=Twist()

    def collison(self,dt):
        print '-------------SENSOR DATA-------------------'
        print 'Range data at 0 deg:   {}'.format(dt.ranges[0])
        print 'Range data at 15 deg:  {}'.format(dt.ranges[15])
        print 'Range data at 345 deg: {}'.format(dt.ranges[345])
        print '-------------------------------------------'

        thr1 = 1 # Laser scan range threshold

        if dt.ranges[0]>thr1 and dt.ranges[15]>thr1 and dt.ranges[345]>thr1: #Checks if there are obstacles in front and 15 degrees left and right (Try changing the the angle values as well as the thresholds)
            #draw circle radious of 5 meter
            self.move.linear.x = 0.5 # go forward (linear velocity)
            self.move.angular.z = 0.1 # rotate (angular velocity)
        else:
            #if there is obstacle turn
            self.move.linear.x = 0.0 # stop
            self.move.angular.z = 0.5 # rotate counter-clockwise
            if dt.ranges[0]>thr1 and dt.ranges[15]>thr1 and dt.ranges[345]>thr1:
                self.move.linear.x = 0.5  # go forward (linear velocity)
                self.move.linear.z = 0.1  # rotate (angular velocity) 

        self.pub.publish(self.move)
        rospy.Rate(0.5)
                   
    #position data from Odometry
    def newOdom(self,msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        print '-------------POSITION DATA-------------------'
        print 'X position:  {}'.format(x)
        print 'Y position:  {}'.format(y)
        print '-------------------------------------------'
    #speed data from Imu  
    def speedvalue(self,data):

        linear_speed=data.linear_acceleration.x
        angular_speed=data.linear_acceleration.z
        print '-------------SPEED DATA-------------------'
        print '-------------------------------------------'
        print 'linear acceleration:   {}'.format(linear_speed)
        print 'angular acceleration:  {}'.format(angular_speed)
        print '-------------------------------------------'
       
        

if __name__ == '__main__':
    rospy.init_node('drawcircle') 
    DrawCircle()
    rospy.spin() 
