cmake_minimum_required(VERSION 3.8)
project(gz_train1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(diagnostic_msgs REQUIRED)
find_package(diagnostic_updater REQUIRED)


add_executable(gz_sub src/gz_sub.cpp)
add_executable(joy1  src/joytest.cpp)
add_executable(slpub src/gz_pub_sleep.cpp)


add_executable(joy2 src/joytest2.cpp)

ament_target_dependencies(
  slpub
  std_msgs
  rclcpp
 
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

  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
launch urdf worlds
DESTINATION share/${PROJECT_NAME})

ament_package()
