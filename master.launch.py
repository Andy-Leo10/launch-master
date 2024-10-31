import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

from launch import LaunchDescription
from launch.actions import (
        IncludeLaunchDescription,
)
from launch.actions import ExecuteProcess
from launch.launch_description_sources import AnyLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

# new imports
from launch.actions import (DeclareLaunchArgument, TimerAction)

def generate_launch_description():
    
    declare_world = DeclareLaunchArgument(
        'world',
        default_value='empty.sdf',
        description='World file to load'
    )
    
    declare_spawn_model_name = DeclareLaunchArgument(
        "model_name", 
        default_value="my_robot",
        description="Model Spawn Name")
    declare_spawn_x = DeclareLaunchArgument(
        "x",
        default_value="0.0",
        description="Model Spawn X Axis Value")
    declare_spawn_y = DeclareLaunchArgument(
        "y",
        default_value="0.0",
        description="Model Spawn Y Axis Value")
    declare_spawn_z = DeclareLaunchArgument(
        "z",
        default_value="0.5",
        description="Model Spawn Z Axis Value")
    
    # headless_arg = DeclareLaunchArgument(
    #     name='headless', 
    #     default_value='false', 
    #     choices=['true', 'false'],
    #     description='Set to true if headless rendering is desired')
    
    ########################### BELOW SIMILAR TO BEFORE ############################
    
    node_world = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(get_package_share_directory( 'rrbot_description' ), 'launch', '2_set_world.launch.py')
        ]),
        launch_arguments={
            'world': LaunchConfiguration('world')
        }.items()
    )
    
    node_spawn_bridge_control = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([
            os.path.join(get_package_share_directory( 'rrbot_description' ), 'launch', '4_spawn_bridge_control.launch.py')
        ]),
    )
        
    # for -> ros2 run PKG EXECUTABLE
    # aan_navigation_clients = ExecuteProcess(
    #     cmd=['ros2', 'run', 'aan_navigation_clients', 'field_cover_client'],
    #     output='screen'
    # )    
    
    ########################### DELAYS TO LAUNCHS ############################
    
    return launch.LaunchDescription([
      
        declare_world,
        node_world,
      
        declare_spawn_model_name,
        declare_spawn_x,
        declare_spawn_y,
        declare_spawn_z,          
        # node_spawn_bridge_control,
        TimerAction(
            period=5.0,
            actions=[node_spawn_bridge_control]
        ),
      
    ])
    
'''
ros2 launch master.launch.py
'''
