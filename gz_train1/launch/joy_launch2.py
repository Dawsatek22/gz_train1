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
        'model', default_value=os.path.join(gazebo_basics_pkg,'urdf','07-physics.urdf'),
        description='Name of the URDF description to load'
    )



    # Define the path to your URDF or Xacro file
    urdf_file_path = PathJoinSubstitution([os.path.join(
        gazebo_basics_pkg,  # Replace with your package name
        "urdf","07-physics.urdf")
    ])
    
 
  
        
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
            gazebo_basics_pkg,
            'worlds',
            'joy_world.sdf'
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v4')],
        'on_exit_shutdown': 'false'}.items()
    )
    
    
    joy = Node(package='gz_train1',
                    namespace='joy_node'
                    ,executable='joy2',
                   remappings=[('/joy', '/keyboard/keypress')],
                    name='joypub1',
                     output='screen')
 
  
    # node that supposed to send  ros2 msgs to the sdf world
    bridge = Node(
    package='ros_gz_bridge',
    executable='parameter_bridge',
    name="joy_bridge",
    namespace='joy_trigger',
    arguments=['/keyboard/keypress@std_msgs/msg/Int32@gz.msgs.Int32'],
    
    remappings=[('/joy', '/keyboard/keypress')],
    output='screen'
   ,
        parameters=[
            {'use_sim_time': True},
        ]
)
                    
    launchDescriptionObject = LaunchDescription()
    launchDescriptionObject.add_action(gazebo_launch)
    launchDescriptionObject.add_action(joy)
    launchDescriptionObject.add_action(bridge)
    

   
    launchDescriptionObject.add_action(gui_arg)
    
    launchDescriptionObject.add_action(rviz_arg)
    
    return launchDescriptionObject