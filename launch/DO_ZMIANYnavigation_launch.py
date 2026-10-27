import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg = get_package_share_directory('description_slambot')
    nav2_dir = get_package_share_directory('nav2_bringup')

    map_arg = DeclareLaunchArgument(
        'map',
        default_value='/home/kamil/ros2_ws/maps/mapa_sciany.yaml',       # !!!   Pełna ścieżka do pliku .yaml mapy   !!!
        description='Pełna ścieżka do pliku .yaml mapy')

    params_arg = DeclareLaunchArgument(
        'params_file',
        default_value=os.path.join(pkg, 'config', 'nav2_params.yaml'),
        description='Parametry Nav2')

    # map_server + AMCL + planner/controller/BT navigator/behaviors itd.
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, 'launch', 'bringup_launch.py')),
        launch_arguments={
            'map': LaunchConfiguration('map'),
            'params_file': LaunchConfiguration('params_file'),
            'use_sim_time': 'True',
            'autostart': 'True',
        }.items())

    return LaunchDescription([map_arg, params_arg, nav2])