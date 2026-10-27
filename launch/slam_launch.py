import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Pobieramy ścieżkę do naszej nowej paczki unitree_navigation
    pkg_share = get_package_share_directory('unitree_navigation') 

    # Poprawna, dynamiczna ścieżka do pliku konfiguracyjnego w folderze config/
    slam_params_file = os.path.join(
        pkg_share, 
        'config', 
        'slam_toolbox_config.yaml'
    )

    slam = Node(
        package="slam_toolbox",
        executable="sync_slam_toolbox_node",
        name="slam_toolbox",
        parameters=[
            slam_params_file,
            {'use_sim_time': True}
        ],
        output="screen"
    )

    return LaunchDescription([
        slam
    ])