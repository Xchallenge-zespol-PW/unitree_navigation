import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource



def generate_launch_description():
    pkg = get_package_share_directory('unitree_navigation')
    nav2_dir = get_package_share_directory('nav2_bringup')

    scan_rotator = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg, 'launch', 'scan_rotation.launch.py')
        )
    )

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg, 'launch', 'slam_launch.py')
        )
    )

    pointcloud_to_laserscan = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg, 'launch', 'pointcloud_to_scan.launch.py')
        )
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'params_file': os.path.join(pkg, 'config', 'nav2_params.yaml'),
            'use_sim_time': 'True',
            'autostart': 'True',
            'use_composition': 'False',
        }.items(),
    )

    

    return LaunchDescription([
        scan_rotator,
        pointcloud_to_laserscan,
        slam,
        # Opóźnienie startu Nav2, żeby SLAM zdążył zainicjalizować mapę i transformacje TF
        TimerAction(period=2.0, actions=[nav2]),
    ])