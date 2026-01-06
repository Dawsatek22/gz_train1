cmake_minimum_required(VERSION 3.8)
project(gz_train1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
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
add_executable(joy1  src/joytest.cpp)
add_executable(slpub src/gz_pub_sleep.cpp)
add_executable(joy2 src/joytest2.cpp)
add_executable(tf2_broad src/tf2_staticbroad_test1.cpp)


ament_python_install_package(${PROJECT_NAME}/scripts)



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
  gz_sub
  std_msgs
  rclcpp
 
)

ament_target_dependencies(
  joy1 
  std_msgs
  rclcpp
 
)

ament_target_dependencies(
  joy2
  std_msgs
  rclcpp
 
)
install(TARGETS  
slpub
joy1
joy2
gz_sub
tf2_broad
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
launch urdf worlds rviz
DESTINATION share/${PROJECT_NAME})


# Install Python executables in the ros2_ws/install/cpp_py_pkg/lib/cpp_py_pkg/ folder
install(PROGRAMS
gz_train1/test_pub.py


DESTINATION lib/${PROJECT_NAME}
)

ament_package()
