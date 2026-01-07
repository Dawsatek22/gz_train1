from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare 


def generate_launch_description():
    ros_gz_sim_pkg_path = FindPackageShare('ros_gz_sim')
    example_pkg_path = FindPackageShare('gz_ltest1')  # Replace with your own package name
    gz_launch_path = PathJoinSubstitution([ros_gz_sim_pkg_path, 'launch', 'ros_gz_sim.launch.py'])

    return LaunchDescription([
       
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={
                'gz_args': [PathJoinSubstitution([example_pkg_path, 'worlds','testbuild3.sdf'])],  # Replace with your own world file
                'on_exit_shutdown': 'True'
            }.items(),
        ),
        
        
        
        

    ])
    