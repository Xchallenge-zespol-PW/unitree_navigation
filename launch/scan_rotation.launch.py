from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    scan_rotator_node = Node(
        package='unitree_navigation',
        executable='scan_rotator.py',
        name='scan_rotator',
        remappings=[
            ('scan_in', '/scan_raw'),
            ('scan_out', '/scan')
        ],
        output='screen'
    )

    return LaunchDescription([
        scan_rotator_node
    ])