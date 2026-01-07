from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription ,DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution,LaunchConfiguration , TextSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition
import os
def generate_launch_description():
    ros_gz_sim_pkg_path = get_package_share_directory('ros_gz_sim')
    example_pkg_path = FindPackageShare('gz_topictest1')  # Replace with your own package name
    world_arg = DeclareLaunchArgument(
        'world', default_value='tworld1.sdf',
        description='Name of the Gazebo world file to load'
    )
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_pkg_path, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
            example_pkg_path,
            'worlds',
            'tworld1.sdf'
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v1')],
        'on_exit_shutdown': 'true'}.items()
    )

    rviz = Node(
       package='rviz2',
       executable='rviz2',
       arguments=['-d', os.path.join(ros_gz_sim_pkg_path, 'rviz', 'diff_drive.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )
    return LaunchDescription([
      gz_sim,
      world_arg
    ])