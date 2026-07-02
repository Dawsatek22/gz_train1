from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import FileContent, LaunchConfiguration, PathJoinSubstitution, TextSubstitution
from launch_ros.actions import Node 
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    main_pkg = get_package_share_directory('gz_train2')
    # ''use_sim_time'' is used to have ros2 use /clock topic for the time source
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf = os.path.join(
      main_pkg,'urdf','test1.urdf')
    with open(urdf,'r') as infp:
        robot = infp.read()
    
   
    declare =   DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
    robotpub =   Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot}],
            arguments=[robot]),
    joint = Node(
            package='gz_train2',
            executable='r2d2',
            name='urdf_joint_cpp',
            output='screen'),
    rviz2 =    Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', 'src/gz_train2/rviz/r2d2 .rviz'],
        parameters=[{
            'use_sim_time': use_sim_time,
        }])
        
        
    gz_world =   IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join('gz_train2', 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
           'src/gz_train2/worlds/rubicon.sdf'
        ]),
        #TextSubstitution(text=' -r -v -v1 --render-engine ogre')],
        TextSubstitution(text=' -r -v -v1')],
        'on_exit_shutdown': 'true'}.items()
    )
    spawn =   Node(package='ros_gz_sim',executable='create',
                 parameters=[{
                    'name': "test1",
                    'x': 1.0,
                    'z': 12.0,
                    'Y': 0.0,
                    'topic': '/robot_description'}]
                 )

        
        
        
    return LaunchDescription([urdf,
   
    ])