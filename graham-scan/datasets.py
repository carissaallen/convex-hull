from math import pi, sqrt, cos, sin
from random import randint, random
from collections import namedtuple
from operator import itemgetter
from time import time

import graham_scan

Point = namedtuple("Point", "x y")
n_points = 100

def benchmark(sizes=[10, 100, 1000, 10000, 100000]):
    """Created as a performance metric."""
    pass


def square_data_set():
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed over a square-shaped interval."""
    ch = graham_scan.ConvexHull()
    for _ in range(n_points):
        ch.add(Point(randint(-100, 100), randint(-100, 100)))
    print("Convex Hull:", ch.get_hull_points())
    ch.display()


def circle_data_set():
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed inside a circle."""
    ch = graham_scan.ConvexHull()
    # R = 5
    for _ in range(n_points):
        t = random() * 2 * pi
        u = random() + random()
        r = 2 - u
        if not u > 1:
            r = u
        # r = R * sqrt(random())
        xy = [r * cos(t), r * sin(t)]
        ch.add(Point(xy[0], xy[1]))
    print("Convex Hull:", ch.get_hull_points())
    ch.display()


def hull_data_set():
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    distributed on the hull."""
    ch = graham_scan.ConvexHull()
    h = 1
    k = 2
    r = 5
    for _ in range(n_points):
        theta = random() * 2 * pi
        x = h + cos(theta) * r
        y = k + sin(theta) * r
        ch.add(Point(x, y))
    print("Convex Hull:", ch.get_hull_points())
    ch.display()
