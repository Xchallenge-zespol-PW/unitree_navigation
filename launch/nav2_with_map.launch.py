import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    pkg = get_package_share_directory('unitree_navigation')
    nav2_dir = get_package_share_directory('nav2_bringup')

    pointcloud_to_laserscan = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg, 'launch', 'pointcloud_to_scan.launch.py')
        )
    )

    # Dynamiczna ścieżka do pliku mapy wewnątrz paczki unitree_navigation/maps/
    default_map_path = os.path.join(pkg, 'maps', 'mapa_sciany.yaml')

    map_arg = DeclareLaunchArgument(
        'map',
        default_value=default_map_path,
        description='Pełna ścieżka do pliku .yaml mapy')

    params_arg = DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(pkg, 'config', 'nav2_params.yaml'),
        description='Parametry Nav2')

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, 'launch', 'bringup_launch.py')),
        launch_arguments={
            'map': LaunchConfiguration('map'),
            'params_file': LaunchConfiguration('params_file'),
            'use_sim_time': 'True',
            'autostart': 'True',
        }.items())

    return LaunchDescription([map_arg, params_arg,
                              pointcloud_to_laserscan,
                              nav2])