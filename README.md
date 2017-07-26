# stt_tool_benchmark 

A set of ROS publisher/subscribers nodes for benchmarking and testing

# Topics:

- Producers are nodes which are producing some data
- Consumers are nodes which requires some data
- Transformers are republishers which subscribes to a topic, do some transformations and republish into another topic

# Services:

- Services will be added in same way as topics

# Use

To start just producers, transformers and producers:
**roslaunch stt_tool_benchmark benchmark.launch**

To start all and do connection examples through topic_tools
**roslaunch stt_tool_benchmark connected.launch**

---

To start a producer / consumer / transformer manually:
rosrun stt_tool_benchmark fahrenheit.py

# Related tools

http://wiki.ros.org/topic_tools
http://wiki.ros.org/topic_tools/relay

rosrun topic_tools relay /producers/temperature/fahrenheit /transformers/input/temperature/fahrenheit

rosrun topic_tools relay /transformers/output/temperature/kelvin /consumers/temperature/kelvin
