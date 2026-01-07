import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import  LaunchConfiguration, PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node

def generate_launch_description():

    world_arg = DeclareLaunchArgument(
        'world', default_value='testbuild3.sdf',
        description='Name of the Gazebo world file to load'
    )

    gz_ltest1 = get_package_share_directory('gz_ltest1')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # Add your own gazebo library path here
   # gazebo_models_path = "/home/d22/gazebo_models"
    #os.environ["GZ_SIM_RESOURCE_PATH"] += os.pathsep + gazebo_models_path


    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
            gz_ltest1,
            'worlds',
            LaunchConfiguration('world')
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v1')],
        'on_exit_shutdown': 'true'}.items()
    )
    
    
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/joy@gz/msgs/Int32.joy'
                   ],
        output='screen'
    )
     
                    
    launchDescriptionObject = LaunchDescription()
    launchDescriptionObject.add_action(world_arg)
    launchDescriptionObject.add_action(gazebo_launch)
    
    launchDescriptionObject.add_action(Node(package='gz_ltest1',
                    namespace='joy'
                    ,executable='pub2',
                    name='joypub'),)
    launchDescriptionObject.add_action(bridge)
    
   

    return launchDescriptionObject