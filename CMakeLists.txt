cmake_minimum_required(VERSION 3.8)
project(unitree_navigation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

# Instalacja folderów launch, config oraz maps, aby były widoczne dla ROS 2
install(DIRECTORY
  launch
  config
  maps
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scan_rotator.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()