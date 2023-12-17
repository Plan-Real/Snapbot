#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time", default="false")
    urdf_file_name = "ur3e.urdf"

    print("urdf_file_name : {}".format(urdf_file_name))

    urdf = os.path.join(
        get_package_share_directory("snapbot_description"), "urdf", urdf_file_name
    )

    # Major refactor of the robot_state_publisher
    # Reference page: https://github.com/ros2/demos/pull/426
    with open(urdf, "r") as infp:
        robot_desc = infp.read()

    rsp_params = {"robot_description": robot_desc}

    rviz_config_dir = os.path.join(
        get_package_share_directory("snapbot_bringup"), "rviz", "model.rviz"
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="false",
                description="Use simulation (Gazebo) clock if true",
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[rsp_params, {"use_sim_time": use_sim_time}],
            ),
            # Node(
            #     package="joint_state_publisher",
            #     executable="joint_state_publisher",
            #     name="joint_state_publisher",
            #     output="screen",
            #     parameters=[rsp_params, {"use_sim_time": use_sim_time}],
            # ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="screen",
                arguments=["-d", rviz_config_dir],
                parameters=[rsp_params, {"use_sim_time": use_sim_time}],
            ),
        ]
    )
