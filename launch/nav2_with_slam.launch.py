import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    unitree_nav_pkg = get_package_share_directory('unitree_navigation')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(unitree_nav_pkg, 'launch', 'slam_launch.py')
        )
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'params_file': os.path.join(unitree_nav_pkg, 'config', 'nav2_params.yaml'),
            'use_sim_time': 'True',
            'autostart': 'True',
            'use_composition': 'False',
        }.items(),
    )

    return LaunchDescription([
        slam,
        
        # Opóźnienie startu Nav2 o 5 sekund, żeby SLAM zdążył zainicjalizować mapę i transformacje TF
        TimerAction(period=5.0, actions=[nav2]),
    ])