from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import FileContent, LaunchConfiguration, PathJoinSubstitution 
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare 
import os

# this is a launch file to learn to spawn a urdf with gazebo.add
# so the comments can  be messy
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command, TextSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_bme_gazebo_basics = get_package_share_directory('gz_train2')
    default_rviz_config_path = PathJoinSubstitution([pkg_bme_gazebo_basics, 'rviz', 'urdf.rviz'])

    main_pkg = FindPackageShare('gz_train2')
    # ''use_sim_time'' is used to have ros2 use /clock topic for the time source
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf = FileContent(
        PathJoinSubstitution([FindPackageShare('gz_train2'), 'urdf', 'r2d2.xacro']))

    return LaunchDescription([
        
        IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
           'empty.sdf'
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v1')],
        'on_exit_shutdown': 'true'}.items()
    ),
        
        Node(package='ros_gz_sim', executable='create',
                 parameters=[{
                    'name': "test1",
                    'x': 1.0,
                    'z': 1.0,
                    'Y': 0.0,
                    'topic': '/robot_description'}],
                 output='screen'),
        
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