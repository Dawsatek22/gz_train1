from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import FileContent, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    main_pkg = FindPackageShare('gz_train2')
    # ''use_sim_time'' is used to have ros2 use /clock topic for the time source
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf = FileContent(
        PathJoinSubstitution([FindPackageShare('gz_train2'), 'urdf', 'r2d2.urdf.xml']))

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': urdf}],
            arguments=[urdf]),
        Node(
            package='gz_train2',
            executable='r2d2',
            name='urdf_joint_cpp',
            output='screen'),
        Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', 'src/gz_train2/rviz/r2d2 .rviz'],
        parameters=[{
            'use_sim_time': use_sim_time,
        }],
    )
    ])