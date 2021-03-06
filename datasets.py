from math import pi, sqrt, cos, sin
from random import randint, random, seed
from collections import namedtuple
from operator import itemgetter
from time import time


import jarvis_march
import graham_scan


Point = namedtuple("Point", "x y")


def square(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed over a square-shaped interval."""
    seed(50)  # use seed to generate repeatable random numbers
    for _ in range(n_points):
        point = Point(randint(-n_points, n_points), randint(-n_points, n_points))
        algorithm.add(point)


def circle(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed inside a circle."""
    points = []
    R = 10
    for _ in range(n_points):
        t = random() * 2 * pi
        r = R * sqrt(random())
        x = r * cos(t)
        y = r * sin(t)
        point = Point(x, y)
        algorithm.add(point)
        points.append(point)
    return points


def triangle(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    distributed inside a triangle."""
    points = []
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
        points.append(point)
    return points


def hull(algorithm, n_points):
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    distributed on the hull."""
    points = []
    h = 1
    k = 2
    r = 5
    for _ in range(n_points):
        theta = random() * 2 * pi
        x = h + cos(theta) * r
        y = k + sin(theta) * r
        point = Point(x, y)
        algorithm.add(point)
        points.append(point)
    return points
