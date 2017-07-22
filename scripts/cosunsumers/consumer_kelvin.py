#!/usr/bin/env python

import rospy, random # Import libraries
import std_msgs.msg # Float from the standard ROS library

# This function is executed after each incoming topic message
def callback(msg):
	rospy.loginfo("Consumer Temperature received Kelvin " + str(msg.data))

rospy.init_node('consumer_kelvin')
rospy.Subscriber("/consumers/temperature/kelvin", std_msgs.msg.Float64, callback)
rospy.spin() # Start and spin server