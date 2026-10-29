#!/usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data

class ScanRotator(Node):
    def __init__(self):
        super().__init__('scan_rotator')

        self.declare_parameter('rotation_angle', math.pi)
        self.rotation_angle = float(
            self.get_parameter('rotation_angle').value
        )

        # Subskrybuje 'scan_in' – dzięki temu remapping z launcha 
        # ('scan_in' -> '/scan_raw') zadziała perfekcyjnie!
        self.subscription = self.create_subscription(
            LaserScan,
            'scan_in',
            self.scan_callback,
            qos_profile_sensor_data
        )

        # Publikuje na 'scan_out' – remapping z launcha 
        # ('scan_out' -> '/scan') skieruje to na właściwy topik.
        self.publisher = self.create_publisher(LaserScan, 'scan_out', qos_profile_sensor_data)

        self.get_logger().info(
            f'ScanRotator uruchomiony: {self.rotation_angle:.6f} rad'
        )

    def scan_callback(self, msg: LaserScan):
        out = LaserScan()
        out.header = msg.header
        
        out.angle_min = msg.angle_min
        out.angle_max = msg.angle_max
        out.angle_increment = msg.angle_increment
        out.time_increment = msg.time_increment
        out.scan_time = msg.scan_time
        out.range_min = msg.range_min
        out.range_max = msg.range_max

        # Jeśli chcesz pełne lustrzane odbicie, zmień list(msg.ranges) na list(reversed(msg.ranges))
        out.ranges = list(reversed(msg.ranges))

        if len(msg.intensities) > 0:
            out.intensities = list(msg.intensities)

        self.publisher.publish(out)

def main(args=None):
    rclpy.init(args=args)
    node = ScanRotator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()