# Introduction to Python

## Description

This project is a part of the "Mechatronic of Mobile Machinery" (Mobil gépek mechatronikája, KOEAA581) course held at the Budapest University of Technology and Economics (BME).
The goal of the project is to provide a quick introduction to Python by implementing a basic map of accumulated pointclouds based on LiDAR and pose data recorded from a robot.

## Data

The `data.json` file contains data recorded from a robot equipped with a 2D LiDAR sensor, exported from ROS.
The data includes LiDAR scans and the robot's 2D pose (x, y, orientation), provided by a localization algorithm.

The structure of the JSON file is as follows:

- **data**: An array of objects, each representing a single timestamped record of the robot's state.
  - **scan**: An array of floating-point numbers representing the distances in meters measured by the 2D LiDAR sensor at various angles. The angles are implicitly represented assuming 1 deg increments from 0 to 359 deg, resulting in 360 captured ranges. `0` corresponds to invalid measurements.
  - **t**: A floating-point number representing the timestamp of the record in seconds since the epoch.
  - **pose**: An array of three floating-point numbers representing the robot's pose in 2D space.
    - The first value represents the x-coordinate in meters.
    - The second value represents the y-coordinate in meters.
    - The third value represents the orientation (theta) of the robot in radians.

## Code, key components

1. Data Loading:
    The function `load_json` is responsible for loading the JSON data from a specified file path.
2. Data Conversion:
    The function `convert_to_polar`  converts raw LiDAR scan data into polar coordinates, filtering out invalid measurements.
3. Data Projection:
    The function `project_to_map_frame` projects the polar scan data to the global map frame using the robot's pose.

Created and captured by Domonkos Csuzdi, BME KJIT, <domonkos.csuzdi@edu.bme.hu>, 2024  
Educational purposes only.
