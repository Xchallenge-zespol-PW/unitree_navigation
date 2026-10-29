from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Węzeł konwertujący chmurę punktów z lidaru na płaski skan 2D /scan
    pointcloud_to_laserscan = Node(
        package='pointcloud_to_laserscan',
        executable='pointcloud_to_laserscan_node',
        name='pointcloud_to_laserscan',
        parameters=[{
            'use_sim_time': True,
            'target_frame': 'pelvis',  # Ramka bazowa humanoida G1
            'transform_tolerance': 0.1,
            'min_height': 0.15,
            'max_height': 1.7,
            'angle_min': -3.14159,
            'angle_max': 3.14159,
            'angle_increment': 0.00436,
            'scan_time': 0.1,
            'range_min': 0.3,
            'range_max': 15.0,
            'use_inf': True,
            'inf_epsilon': 1.0,
        }],
        remappings=[('cloud_in', '/lidar/points'), ('scan', '/scan_raw')],
    )

    return LaunchDescription([
        pointcloud_to_laserscan
    ])