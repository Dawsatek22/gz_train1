#here is the cmake list
cmake_minimum_required(VERSION 4.2.1)
project(gz_train1)
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake_pytest REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(diagnostic_msgs REQUIRED)
find_package(diagnostic_updater REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rclpy REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
include_directories(include)
add_executable(gz_sub src/gz_sub.cpp)
add_executable(joy  src/joytest.cpp)
add_executable(slpub src/gz_pub_sleep.cpp)
add_executable(joy2 src/joytest2.cpp)
add_executable(tf2_broad src/tf2_staticbroad_test1.cpp)
add_executable(lpub src/loop_pub.cpp)



ament_target_dependencies(
 slpub
 geometry_msgs
  std_msgs
  rclcpp
)


ament_target_dependencies(
 tf2_broad
 geometry_msgs
   rclcpp
   tf2
   tf2_ros
)
ament_target_dependencies(
  lpub
  std_msgs
  rclcpp
 
)

ament_target_dependencies(
  gz_sub
  std_msgs
  rclcpp
 
)

ament_target_dependencies(
  joy
  std_msgs
  rclcpp
 
)

ament_target_dependencies(
  joy2
  std_msgs
  rclcpp
 
)


#ament_python_install_package(${PROJECT_NAME})


  install(TARGETS  
  lpub
  gz_sub
  joy
  joy2
  tf2_broad
  slpub


  
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
launch urdf worlds rviz  scripts
DESTINATION share/${PROJECT_NAME})




ament_package()
