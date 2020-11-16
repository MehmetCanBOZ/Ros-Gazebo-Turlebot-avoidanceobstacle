# Ros-Gazebo-Turlebot-avoidanceobstacle
Gazebo turtlebot 

Following the beginner tutorials
(http://wiki.ros.org/ROS/Tutorials), bring up a two-wheeled, non-holonomic ground robot (preferably
TurtleBot or RosBot) in Gazebo. Also, bring some environment objects such as tables, chairs, blocks,
etc. in Gazebo. Write a class file in a python script (main.py) which acquires the IMU, odometry,
LIDAR, and Kinect stereo callbacks and publishes the motion command to the robot. Draw a circle
trajectory of radius 5 meters with the robot by giving a suitable linear and angular velocity. The robot
should always observe the environment with its LIDAR sensor, and if there is an obstacle on the robot’s
trajectory, then it should avoid a collision (it may cease the trajectory following objective). For this
purpose, you may reduce the linear speed and change the angular velocity of the robot. You need to
write the collision avoidance part as a separate function.
