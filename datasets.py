from math import pi, sqrt, cos, sin
from random import randint, random, seed
from collections import namedtuple
from operator import itemgetter
from time import time


import jarvis_march
import graham_scan


Point = namedtuple("Point", "x y")


def benchmark(sizes=[10, 100, 1000, 10000, 100000]):
    """Created as a performance metric."""
    pass


def square_data_set(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed over a square-shaped interval."""
    seed(50)  # use seed to generate repeatable random numbers
    for _ in range(n_points):
        point = Point(randint(-n_points, n_points), randint(-n_points, n_points))
        algorithm.add(point)


def circle_data_set(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed inside a circle."""
    R = 10
    for _ in range(n_points):
        t = random() * 2 * pi
        r = R * sqrt(random())
        x = r * cos(t)
        y = r * sin(t)
        point = Point(x, y)
        algorithm.add(point)
    print(algorithm.points)


def hull_data_set(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    distributed on the hull."""
    h = 1
    k = 2
    r = 5
    for _ in range(n_points):
        theta = random() * 2 * pi
        x = h + cos(theta) * r
        y = k + sin(theta) * r
        point = Point(x, y)
        algorithm.add(point)


def triangle_data_set(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    distributed inside a triangle."""
    p1 = (1, 1)
    p2 = (2, 4)
    p3 = (5, 2)
    for _ in range(n_points):
        s, t = sorted([random(), random()])
        (
            s * p1[0] + (t - s) * p2[0] + (1 - t) * p3[0],
            s * p1[1] + (t - s) * p2[1] + (1 - t) * p3[1],
        )
        point = Point(s, t)
        algorithm.add(point)
