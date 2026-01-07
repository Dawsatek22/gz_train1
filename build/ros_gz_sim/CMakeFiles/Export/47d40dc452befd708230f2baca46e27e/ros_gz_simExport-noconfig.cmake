#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ros_gz_sim::ros_gz_sim" for configuration ""
set_property(TARGET ros_gz_sim::ros_gz_sim APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ros_gz_sim::ros_gz_sim PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libros_gz_sim.so"
  IMPORTED_SONAME_NOCONFIG "libros_gz_sim.so"
  )

list(APPEND _cmake_import_check_targets ros_gz_sim::ros_gz_sim )
list(APPEND _cmake_import_check_files_for_ros_gz_sim::ros_gz_sim "${_IMPORT_PREFIX}/lib/libros_gz_sim.so" )

# Import target "ros_gz_sim::ros_gz_sim_spawn_entity" for configuration ""
set_property(TARGET ros_gz_sim::ros_gz_sim_spawn_entity APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ros_gz_sim::ros_gz_sim_spawn_entity PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libros_gz_sim_spawn_entity.so"
  IMPORTED_SONAME_NOCONFIG "libros_gz_sim_spawn_entity.so"
  )

list(APPEND _cmake_import_check_targets ros_gz_sim::ros_gz_sim_spawn_entity )
list(APPEND _cmake_import_check_files_for_ros_gz_sim::ros_gz_sim_spawn_entity "${_IMPORT_PREFIX}/lib/libros_gz_sim_spawn_entity.so" )

# Import target "ros_gz_sim::ros_gz_sim_set_entity_pose" for configuration ""
set_property(TARGET ros_gz_sim::ros_gz_sim_set_entity_pose APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ros_gz_sim::ros_gz_sim_set_entity_pose PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libros_gz_sim_set_entity_pose.so"
  IMPORTED_SONAME_NOCONFIG "libros_gz_sim_set_entity_pose.so"
  )

list(APPEND _cmake_import_check_targets ros_gz_sim::ros_gz_sim_set_entity_pose )
list(APPEND _cmake_import_check_files_for_ros_gz_sim::ros_gz_sim_set_entity_pose "${_IMPORT_PREFIX}/lib/libros_gz_sim_set_entity_pose.so" )

# Import target "ros_gz_sim::ros_gz_sim_delete_entity" for configuration ""
set_property(TARGET ros_gz_sim::ros_gz_sim_delete_entity APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ros_gz_sim::ros_gz_sim_delete_entity PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libros_gz_sim_delete_entity.so"
  IMPORTED_SONAME_NOCONFIG "libros_gz_sim_delete_entity.so"
  )

list(APPEND _cmake_import_check_targets ros_gz_sim::ros_gz_sim_delete_entity )
list(APPEND _cmake_import_check_files_for_ros_gz_sim::ros_gz_sim_delete_entity "${_IMPORT_PREFIX}/lib/libros_gz_sim_delete_entity.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
