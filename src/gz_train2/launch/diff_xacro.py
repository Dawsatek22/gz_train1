
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
import xacro
def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_bme_gazebo_basics = get_package_share_directory('gz_train2')
    default_rviz_config_path = PathJoinSubstitution([pkg_bme_gazebo_basics, 'rviz', 'rviz/gz_train2_xacro.rviz'])

  
    # URDF model path to spawn urdf file in gazebo
  


        # Define the path to your URDF or Xacro file
    urdf = os.path.join(
        pkg_bme_gazebo_basics ,'urdf/my_robot.urdf.xacro')
    
    urdf2 = xacro.process_file(urdf).toxml()
    with open(urdf,'r') as infp:
        robot = infp.read()
    
    
    
        
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
           'src/gz_train2/worlds/testworld1.sdf'
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v1')],
        'on_exit_shutdown': 'true'}.items()
    )
    
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description':  urdf2,
             'use_sim_time': True},
        ],
        
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
    )
    
    spawn = Node(package='ros_gz_sim', executable='create',
                 parameters=[{
                    'name': "test1",
                    'x': 1.0,
                    'z': 12.0,
                    'Y': 0.0,
                    'topic': '/robot_description'}],
                 output='screen')
    
    joy = Node(package='gz_train1',
                    namespace='joytest'
                    ,executable='joy1',
                    name='joypub'),
    rvizz  = Node(
        package="rviz2",
        executable="rviz2",
       #  arguments=['-d', default_rviz_config_path]
    )
    return  LaunchDescription([rvizz,robot_state_publisher_node,spawn,joint_state_publisher_gui_node,
                               gazebo_launch])
    src/gz_train2/urdf/my_robot.urdf.xacro