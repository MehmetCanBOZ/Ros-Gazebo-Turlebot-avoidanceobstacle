
class DrawCircle():

	def __init__(self):
        
		rospy.init_node('drawcircle', anonymous=False) 
        rospy.on_shutdown(self.shutdown) # Type Ctrl+C to shut it down 
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        r = rospy.Rate(20); #Frequency
        #SPEED & ANGLE ADJUSTMENT
        turn_cmd = Twist()
        turn_cmd.linear.x = 0.2 #linear
        a = 20 #angle
        turn_cmd.angular.z = radians(a); #angular

        #START MOVING
        while not rospy.is_shutdown():
        	rospy.loginfo("Circling")
            for x in range(0,(360/a)):
        	self.cmd_vel.publish(turn_cmd)
    	    r.sleep() 

#STOP
    def shutdown(self):
    	rospy.loginfo("Stop Circling")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
	try:
		DrawCircle()
	except:
		rospy.loginfo("node terminated.")
