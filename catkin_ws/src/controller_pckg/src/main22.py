#!/usr/bin/env python
import rospy # Python library for ROS
from sensor_msgs.msg import LaserScan # LaserScan type message is defined in sensor_msgs
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry

class Circling(): #main class
   
    def __init__(self): #main function
        global circle
        circle = Twist() #create object of twist type  
        rate = rospy.Rate(5)      
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #publish message
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback)  #subscribe message 
        self.sub = rospy.Subscriber("/odom", Odometry, self.odometry)

    def callback(self, msg): #function for obstacle avoidance
        print '-------RECEIVING LIDAR SENSOR DATA-------'
        print 'Front: {}'.format(msg.ranges[0]) #lidar data for front side
        print 'Left:  {}'.format(msg.ranges[90]) #lidar data for left side
        print 'Right: {}'.format(msg.ranges[270]) #lidar data for right side
        print 'Back: {}'.format(msg.ranges[180]) #lidar data for back side
      
      	#Obstacle Avoidance
        self.distance = 0.7
        if msg.ranges[0] > self.distance and msg.ranges[15] > self.distance and msg.ranges[345] > self.distance: 
        #when no any obstacle near detected
            circle.linear.x = 0.5 #linear velocity
            circle.angular.z = 0.1 #angular velocity
            rospy.loginfo("Circling") #state situation constantly
        else: #when an obstacle near detected
            rospy.loginfo("An Obstacle Near Detected") #state case of detection
            circle.linear.x = 0.0 # stop
            circle.angular.z = 0.5 # rotate counter-clockwise
            if msg.ranges[0] > self.distance and msg.ranges[15] > self.distance and msg.ranges[345] > self.distance and msg.ranges[45] > self.distance and msg.ranges[315] > self.distance:
                #when no any obstacle near detected after rotation
                circle.linear.x = 0.5
                circle.angular.z = 0.1
        self.pub.publish(circle) # publish the move object
        rospy.Rate(1)

    def odometry(self, msg):
        print msg.pose.pose

if __name__ == '__main__':
    rospy.init_node('obstacle_avoidance_node') #initilize node
    Circling()
    rospy.spin() #loop it