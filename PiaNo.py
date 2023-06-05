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
        alpha = np.random.uniform(0, 2 * np.pi)

        x_2 = x_1 + a * np.cos(alpha)
        y_2 = y_1 + a * np.sin(alpha)

        points_2.append((x_2, y_2))

points(N)

#plot the lines betwen the points in only one plot
def plot_lines(N):
    for i in range(N):
        plt.plot([points_1[i][0], points_2[i][0]], [points_1[i][1], points_2[i][1]], 'r')
    plt.show()

plot_lines(N)