#!/usr/bin/env python

# This node publishes a temperature in Fahrenheit degrees

import rospy, random # Import libraries
import std_msgs.msg  # Float from the standard ROS library

herz = 10 # 10hz publishing rate

# Topic name to publish:
pub = rospy.Publisher('/producers/temperature/fahrenheit', std_msgs.msg.Float64, queue_size=10)

# Node name of the publisher:
rospy.init_node('producer_temperature_fahrenheit')

r = rospy.Rate(herz) # Rate obtained from hertz
while not rospy.is_shutdown():
	temperature = random.uniform(0, 80)
	pub.publish(temperature)
	r.sleep()