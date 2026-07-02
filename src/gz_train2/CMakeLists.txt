cmake_minimum_required(VERSION 4.2.1)
project(gz_train2)


if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies


find_package(ros2_control_cmake REQUIRED)
set_compiler_options()
export_windows_symbols()

# find dependencies
set(THIS_PACKAGE_INCLUDE_DEPENDS
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
)


find_package(controller_manager 4.0.0)
# Handle the case where the required version is not found
if(NOT controller_manager_FOUND)
  message(FATAL_ERROR "ros2_control version 4.0.0 or higher is required. "
  "Are you using the correct branch of the ros2_control_demos repository?")
endif()


# find dependencies
find_package(backward_ros REQUIRED)
find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()



find_package(ament_cmake_pytest REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
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
add_executable(param_pub src/param_publisher.cpp )
find_package(tf2_geometry_msgs REQUIRED)
add_executable(joint1 src/joint_test.cpp)
add_executable(r2d2 src/r2d2_joint.cpp)
ament_target_dependencies(
 param_pub

  std_msgs
  rclcpp
)

ament_target_dependencies(
 slpub
 geometry_msgs
  std_msgs
  rclcpp
)


ament_target_dependencies(
 r2d2
 sensor_msgs
 geometry_msgs
  std_msgs
  rclcpp
  tf2_ros
  tf2 
  tf2_geometry_msgs
)


ament_target_dependencies(
 joint1
 sensor_msgs
 geometry_msgs
  std_msgs
  rclcpp
  tf2_ros
  tf2 
  tf2_geometry_msgs
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
  r2d2
  param_pub
  lpub
  gz_sub
  joy
  joy2
  tf2_broad
  slpub

joint1
  
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
launch urdf worlds rviz   TurtleBot turtlebot3Burger  dx_bot config
DESTINATION share/${PROJECT_NAME})




ament_package()
