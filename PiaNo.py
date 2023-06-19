import random
import numpy as np
import math
import matplotlib.pyplot as plt

a = 0.06
points_1 = []
points_2 = []
N = 100

#create a list of N tuple with the coordinates of the points
def points(N):
    for i in range(N):
        x_1 = np.random.uniform(0, 1)
        y_1 = np.random.uniform(0, 1)
        points_1.append((x_1, y_1))
        
        alpha_value = np.random.uniform(0, 2 * np.pi)
        alphas.append(alpha_value)

        x_2 = x_1 + a * np.cos(alpha_value)
        y_2 = y_1 + a * np.sin(alpha_value)

        points_2.append((x_2, y_2))

points(N)

#plot the lines betwen the points in only one plot
def plot_lines(N):
    # Define custom colors
    line_color = 'steelblue'
    marker_color = 'none'

    # Define marker style for data points
    marker_style = 'o'
    marker_size = 8

    # Calculate plot limits
    x_min = min(min(points_1[i][0], points_2[i][0]) for i in range(N))
    x_max = max(max(points_1[i][0], points_2[i][0]) for i in range(N))
    y_min = min(min(points_1[i][1], points_2[i][1]) for i in range(N))
    y_max = max(max(points_1[i][1], points_2[i][1]) for i in range(N))

    # Set figure size
    plt.figure(figsize=(8, 6))

    for i in range(N):
        # Plot lines between points
        plt.plot([points_1[i][0], points_2[i][0]], [points_1[i][1], points_2[i][1]], linestyle='-', color=line_color)

        # Plot data points without markers
        plt.scatter(points_1[i][0], points_1[i][1], marker=marker_style, s=marker_size, color=marker_color)
        plt.scatter(points_2[i][0], points_2[i][1], marker=marker_style, s=marker_size, color=marker_color)

    # Customize grid
    plt.grid(True, linestyle='dotted', linewidth=0.5, color='gray')

    # Set labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Lines between Points')

    # Adjust plot limits
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Display the plot
    plt.show()

#Regions

def is_point_inside_region_1(x, y, theta, a):
    # Check if x ∈ [0, a/2]
    if x < 0 or x > a/2:
        return False

    # Calculate the bounds for y based on x
    y_lower_bound = -math.sqrt(a**2 - (x - a)**2) + a
    y_upper_bound = a

    # Check if y ∈ [-sqrt(a**2 - (x-a)**2) + a, a]
    if y < y_lower_bound or y > y_upper_bound:
        return False

    # Calculate the bounds for theta based on x and y
    theta_lower_bound = math.atan((a - y) / (a - x))
    theta_upper_bound = math.pi/2 + math.atan(x / (a - y))

    # Normalize theta to be in the range [0, 2π)
    normalized_theta = theta % (2 * math.pi)

    # Normalize the bounds for theta to the same range
    normalized_theta_lower_bound = theta_lower_bound % (2 * math.pi)
    normalized_theta_upper_bound = theta_upper_bound % (2 * math.pi)

    # Check if theta ∈ [arctan((a - y)/(a - x)), π/2 + arctan(x/(a - y))]
    if normalized_theta_lower_bound <= normalized_theta <= normalized_theta_upper_bound:
        return True

    return False

def is_point_inside_region_2(x, y, theta, a):
    # Check if x ∈ [0, a/2]
    if x < 0 or x > a/2:
        return False

    # Calculate the bounds for y based on x
    y_lower_bound = -math.sqrt(a**2 - x**2) + a
    y_upper_bound = -math.sqrt(a**2 - (x - a)**2) + a

    # Check if y ∈ [-sqrt(a**2 - x**2) + a, -sqrt(a**2 - (x - a)**2) + a]
    if y < y_lower_bound or y > y_upper_bound:
        return False

    # Calculate the bounds for theta based on x and y
    theta_lower_bound = math.asin((a - y) / a)
    theta_upper_bound = math.pi/2 + math.atan(x / (a - y))

    # Normalize theta to be in the range [0, 2π)
    normalized_theta = theta % (2 * math.pi)

    # Normalize the bounds for theta to the same range
    normalized_theta_lower_bound = theta_lower_bound % (2 * math.pi)
    normalized_theta_upper_bound = theta_upper_bound % (2 * math.pi)

    # Check if theta ∈ [arcsin((a - y)/a), π/2 + arctan(x/(a - y))]
    if normalized_theta_lower_bound <= normalized_theta <= normalized_theta_upper_bound:
        return True

    return False

def is_point_inside_region_3(x, y, theta, a):
    # Check if x ∈ [0, a/2]
    if x < 0 or x > a/2:
        return False

    # Calculate the upper bound for y based on x
    y_upper_bound = -math.sqrt(a**2 - x**2) + a

    # Check if y ∈ [0, -sqrt((a**2 - x**2)) + a]
    if y < 0 or y > y_upper_bound:
        return False

    # Calculate the bounds for theta based on y
    try:
        theta_lower_bound = math.asin((a - y) / a)
        theta_upper_bound = math.pi - math.asin((a - y) / a)
    except ValueError:
        return False

    # Normalize theta to be in the range [0, 2π)
    normalized_theta = theta % (2 * math.pi)

    # Normalize the bounds for theta to the same range
    normalized_theta_lower_bound = theta_lower_bound % (2 * math.pi)
    normalized_theta_upper_bound = theta_upper_bound % (2 * math.pi)

    # Check if theta ∈ [arcsin((a - y)/a), π - arcsin((a - y)/a)]
    if normalized_theta_lower_bound <= normalized_theta <= normalized_theta_upper_bound:
        return True

    return False

def is_point_inside_region_4(x, y, theta, a):
    # Check if x ∈ [0, a/2]
    if x < 0 or x > a/2:
        return False

    # Calculate the upper bound for y based on x
    try:
        y_upper_bound = math.sqrt(a**2 - (x - a)**2)
    except ValueError:
        return False

    # Check if y ∈ [0, sqrt(a**2 - (x - a)**2)]
    if y < 0 or y > y_upper_bound:
        return False

    try:
        # Calculate the bounds for theta based on x and y
        theta_lower_bound = math.atan(y / (a - x))
        theta_upper_bound = math.pi - math.acos((a - x) / x)
    except (ValueError, ZeroDivisionError):
        return False

    # Normalize theta to be in the range [0, 2π)
    normalized_theta = theta % (2 * math.pi)

    # Normalize the bounds for theta to the same range
    normalized_theta_lower_bound = theta_lower_bound % (2 * math.pi)
    normalized_theta_upper_bound = theta_upper_bound % (2 * math.pi)

    # Check if theta ∈ [arctan(y/(a - x)), π - arccos((a - x)/x)]
    if normalized_theta_lower_bound <= normalized_theta <= normalized_theta_upper_bound:
        return True

    return False

#Given a array of points (x, y) and array of angles, and a value a, create a function in python to identify if a line has intersections points with all the other lines 
#find intersections using theta = theta1 - theta 2 and x = x1,2 - x1,1, y = y1,2 - y1,1
#find the intersection points of the lines
def find_intersections(points, angle, a):
    # Find the intersection points of the lines
    intersections = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Calculate the angle between the lines
            theta = angle[i] - angle[j]

            # Calculate the difference in x and y between the lines
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]

            # Check if the lines intersect
            if is_point_inside_region_1(x, y, theta, a):
                print("There is an intersection point in region I")
            elif is_point_inside_region_2(x, y, theta, a):
                print("There is an intersection point in region II")
            elif is_point_inside_region_3(x, y, theta, a):
                print("There is an intersection point in region III")
            elif is_point_inside_region_4(x, y, theta, a):
                print("There is an intersection point in region IV")
            else:
                print("There is no intersection point")




            
                
                
                or is_point_inside_region_2(x, y, theta, a) or is_point_inside_region_3(x, y, theta, a) or is_point_inside_region_4(x, y, theta, a):
                intersections.append((i, j))

    return intersections

plot_lines(N)