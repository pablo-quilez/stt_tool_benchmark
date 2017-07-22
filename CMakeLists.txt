cmake_minimum_required(VERSION 2.8.3)
project(stt_tool_benchmark)

find_package(catkin REQUIRED COMPONENTS genmsg std_msgs message_generation)

generate_messages(  
  DEPENDENCIES std_msgs
)

catkin_package(
  CATKIN_DEPENDS std_msgs
)
