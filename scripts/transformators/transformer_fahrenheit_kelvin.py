#!/usr/bin/env python

import rospy, random # Import libraries
import std_msgs.msg  # Float from the standard ROS library

# This function is executed after each incoming topic message
def callback(msg):
	rospy.loginfo("Transformer Temperature received Fahrenheit " + str(msg.data))
	publisher.publish((msg.data+459.67)*5.0/9)

rospy.init_node('stt_test_topics')
publisher = rospy.Publisher('/transformers/output/temperature/kelvin', std_msgs.msg.Float64, queue_size=10)
rospy.Subscriber("/transformers/input/temperature/fahrenheit", std_msgs.msg.Float64, callback)

rospy.spin() # Start and spin server