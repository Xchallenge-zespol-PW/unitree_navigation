import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg = get_package_share_directory('description_slambot')
    nav2_dir = get_package_share_directory('nav2_bringup')

    # slam_toolbox: publikuje /map oraz TF map -> odom
    # (Twój slam_launch.py; użyj wersji ASYNC z mapper_params_online_async.yaml)
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg, 'launch', 'slam_launch.py')))

    # Sama nawigacja: planner, controller, bt_navigator, behaviors, smoother.
    # BEZ map_server i AMCL (to robi slam_toolbox).
    # use_composition=False, bo kontener tworzy bringup_launch.py, a tu go nie używamy.
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, 'launch', 'navigation_launch.py')),
        launch_arguments={
            'params_file': os.path.join(pkg, 'config', 'nav2_params.yaml'),
            'use_sim_time': 'True',
            'autostart': 'True',
            'use_composition': 'False',
        }.items())

    # Nav2 startuje z opóźnieniem, żeby slam_toolbox zdążył opublikować
    # pierwszą mapę i transformatę map -> odom
    return LaunchDescription([
        slam,
        TimerAction(period=5.0, actions=[nav2]),
    ])