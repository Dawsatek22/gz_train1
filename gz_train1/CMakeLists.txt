cmake_minimum_required(VERSION 3.8)
project(gz_train1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(joy1  src/joytest.cpp)

ament_target_dependencies(
  joy1 
  std_msgs
  rclcpp
 
)
install(TARGETS  
joy1
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
launch urdf worlds
DESTINATION share/${PROJECT_NAME})

ament_package()
