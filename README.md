# Unitree Navigation & Scan Rotator

ROS 2 package for handling laser scans on Unitree G1 (specifically configured for inverted LiDAR setups using a custom scan rotation/mirroring node).

---

## Prerequisites & Dependencies

This package requires the `pointcloud_to_laserscan` package to convert raw point clouds into laser scans. 

Navigate to your workspace's `src` directory and clone the compatible branch (Humble/Iron/Jazzy depending on your distro):

```bash
cd ~/ros2_ws/src
git clone [https://github.com/ros-perception/pointcloud_to_laserscan.git](https://github.com/ros-perception/pointcloud_to_laserscan.git) -b humble
