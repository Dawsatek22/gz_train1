# this is a launch file to learn to spawn a urdf with gazebo and publish ros2 joystick msgs to gazebo
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
    gazebo_basics_pkg = get_package_share_directory('gz_train1')
    default_rviz_config_path = PathJoinSubstitution([gazebo_basics_pkg, 'rviz', 'urdf.rviz'])

    # Show joint state publisher GUI for joints
    gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    
    # RViz config file path
    rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                    description='Absolute path to rviz config file')
    
   
    # URDF model path to spawn urdf file in gazebo
    model_arg = DeclareLaunchArgument(
        'model', default_value=os.path.join(gazebo_basics_pkg,'urdf','08-macroed.urdf.xacro'),
        description='Name of the URDF description to load'
    )

    # Use built-in ROS2 URDF launch package with our own arguments
    urdf_rviz = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'gz_train1',
            'urdf_package_path': PathJoinSubstitution([gazebo_basics_pkg,'urdf', '08-macroed.urdf.xacro']),
            'rviz_config': LaunchConfiguration('rvizconfig'),
            'jsp_gui': LaunchConfiguration('gui')}.items()
    )


    # Define the path to your URDF or Xacro file
    urdf_file_path = PathJoinSubstitution([os.path.join(
        gazebo_basics_pkg,  # Replace with your package name
        "urdf","08-macroed.urdf.xacro")
    ])
    
 
        
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
            gazebo_basics_pkg,
            'worlds',
            'testbuild3.sdf'
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v1')],
        'on_exit_shutdown': 'true'}.items()
    )
    # the node that publish the robot state  
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description':  urdf_file_path,
             'use_sim_time': True},
        ],
        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static')
        ]
    )
    # gui for the robot publisher
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
    )
    # node to spawn robot model
    spawn = Node(package='ros_gz_sim', executable='create',
                 parameters=[{
                    'name': "test_model1",
                    '-file':urdf_file_path,
                    'x': 5.0,
                    'z': 0.6,
                    'Y': 2.0,
                    'topic': '/robot_description'}],
                 output='screen')
  # node that publish joystick msgs
    joy = Node(package='gz_train1',
                    namespace='joy'
                    ,executable='joy1',
                    name='joypub')
    # node that supposed to send  ros2 msgs to the sdf world
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/joy@gz/msgs/Int32.joy'
                   ],
        output='screen'
    )
     
                    
    launchDescriptionObject = LaunchDescription()
   
    
    launchDescriptionObject.add_action(gazebo_launch)
    launchDescriptionObject.add_action(bridge)
    launchDescriptionObject.add_action(joy)
    launchDescriptionObject.add_action(gui_arg)
    
    launchDescriptionObject.add_action(rviz_arg)
    launchDescriptionObject.add_action(model_arg)
    launchDescriptionObject.add_action(urdf_rviz)
    launchDescriptionObject.add_action(spawn)
    launchDescriptionObject.add_action(robot_state_publisher_node)
    launchDescriptionObject.add_action(joint_state_publisher_gui_node)
    return launchDescriptionObject