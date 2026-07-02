
# this is a launch file to learn to spawn a urdf with gazebo.add
# so the comments can  be messy
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution,PathSubstitution, Command, TextSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch_ros.substitutions import FindPackageShare
import xacro
def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_bme_gazebo_basics = get_package_share_directory('gz_train2')
    default_rviz_config_path = PathJoinSubstitution([pkg_bme_gazebo_basics, 'rviz', 'rviz/gz_train2_xacro.rviz'])
   
    main_pkg = get_package_share_directory(package_name='gz_train2',print_warning=True) # package directory



     # Gazebo hint for resources.
    os.environ['GZ_SIM_RESOURCE_PATH'] = pkg_ros_gz_sim

    path_to_share_dir_clipped = get_package_share_directory("gz_train2")

    
    # Ensure `SDF_PATH` is populated since `sdformat_urdf` uses this rather

    # than `GZ_SIM_RESOURCE_PATH` to locate resources.
    if "GZ_SIM_RESOURCE_PATH" in os.environ:
        gz_sim_resource_path = os.environ["GZ_SIM_RESOURCE_PATH"]

        if "SDF_PATH" in os.environ:
            sdf_path = os.environ["SDF_PATH"]
            os.environ["SDF_PATH"] = sdf_path + ":" + gz_sim_resource_path
        else:
            os.environ["SDF_PATH"] = gz_sim_resource_path



        # Define the path to your URDF or Xacro file
    urdf = os.path.join(
        main_pkg,'urdf/rrbot_1wrapper.xacro')
    
    urdf2 = xacro.process_file(urdf).toxml()
    
    
    
        
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={'gz_args': [PathJoinSubstitution([
           'empty.sdf'
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
                    'z': 0.0,
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
         arguments=['-d', 'src/gz_train2/rviz/rrbot_xacro.rviz']
    )
    
    rc_controller = Node(
                package="controller_manager",
                executable="spawner",
                arguments=[
                    "joint_state_broadcaster",
                    "--param-file",
                    PathSubstitution(FindPackageShare("gz_train2"))
                    ,"config/rrbot_control1.yaml"
                ],
            ),
    rc_joint1 =  Node(
                package="ros2_controllers_test_nodes",
                executable="publisher_joint_trajectory_controller",
                name="publisher_joint_trajectory_controller",
                parameters=[
                    "src/gz_train2/config/rrbot_joint_trajectory_test1.yaml"
                ],
                output="screen",
            )
    
    return  LaunchDescription([rvizz,rc_joint1,robot_state_publisher_node,spawn,joint_state_publisher_gui_node,
                               gazebo_launch])
    src/gz_train2/urdf/my_robot.urdf.xacro