# Domonkos Csuzdi, BME KJIT, domonkos.csuzdi@edu.bme.hu, 2024-09-10
# Educational purposes only.

import json
import numpy as np
import matplotlib.pyplot as plt

from customtype.pose import Pose2D


def load_json(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data["data"]


def convert_to_polar(scan_data):
    """
    Creates (angle, range) tuples from the scan data,
    assuming the ranges (scan data) are in order of increasing angle.
    The LiDAR returns 0 for invalid measurements, so we filter out those.
    """

    angles = np.linspace(0, 2 * np.pi, len(scan_data))
    polar_scan = [
        (angle, range) for angle, range in zip(angles, scan_data) if range > 0
    ]
    return polar_scan


def project_to_map_frame(robot_pose: Pose2D, polar_scan):
    """
    The LiDAR scans are in the robot's (local) frame of reference.
    This function projects the polar scan data to the map (global) frame,
    given the robot's pose.
    """

    x_global = np.zeros([len(polar_scan), 2])  # x,y coordinates of the projected points

    # unpack the polar data:
    # bit redundant given the previous function,
    # but good for clarity and practice of list comprehensions
    angles = np.array([polar[0] for polar in polar_scan])
    ranges = np.array([polar[1] for polar in polar_scan])

    # basic trigonometry of polar to cartesian,
    # and adding the robot's pose to get the global coordinates
    angles_global = angles + robot_pose.theta
    r_cos = ranges * np.cos(angles_global)
    r_sin = ranges * np.sin(angles_global)

    x_global[:, 0] = r_cos + robot_pose.x
    x_global[:, 1] = r_sin + robot_pose.y

    return x_global


def process_and_plot_data(records):

    # plotting could be done in a separate function
    fig = plt.figure()
    ax = fig.add_subplot()

    for record in records:
        pose_data = record["pose"]
        pose = Pose2D(pose_data[0], pose_data[1], pose_data[2])
        # pose = Pose2D(*pose_data)

        scan_data = record["scan"]
        polar_data = convert_to_polar(scan_data)
        point_cloud = project_to_map_frame(pose, polar_data)

        ax.scatter(point_cloud[:, 0], point_cloud[:, 1], s=0.001, c="b", alpha=0.5)

    plt.show()
    # sometimes the graphic backend is not present, so install the PyQt5 package
    # via `pip install PyQt5`


def main():
    pose1 = Pose2D(1, 2, 3)

    print(pose1.convert_to_deg())

    # test the __str__ method
    print(pose1)

    records = load_json("data.json")
    process_and_plot_data(records)


if __name__ == "__main__":
    main()
