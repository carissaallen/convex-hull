from math import pi, sqrt, cos, sin
from random import randint, random, seed
from collections import namedtuple
from operator import itemgetter
from time import time

import jarvis_march
import graham_scan


Point = namedtuple("Point", "x y")
n_points = 10


def benchmark(sizes=[10, 100, 1000, 10000, 100000]):
    """Created as a performance metric."""
    pass


def square_data_set():
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed over a square-shaped interval."""
    graham = graham_scan.GrahamScan()
    jarvis = jarvis_march.JarvisMarch()
    seed(33)  # use seed to generate repeatable random numbers
    for _ in range(n_points):
        point = Point(randint(-100, 100), randint(-100, 100))
        graham.add(point)
        jarvis.add(point)
    print("Convex Hull:", graham.get_hull_points())
    graham.display()
    print("Convex Hull:", jarvis.get_hull_points())
    jarvis.display()


def circle_data_set():
    """Input data for the Convex Hull program are coordinates of the points (random integers)
    uniformly distributed inside a circle."""
    graham = graham_scan.GrahamScan()
    jarvis = jarvis_march.JarvisMarch()
    # R = 5
    for _ in range(n_points):
        t = random() * 2 * pi
        u = random() + random()
        r = 2 - u
        if not u > 1:
            r = u
        # r = R * sqrt(random())
        xy = [r * cos(t), r * sin(t)]
        point = Point(xy[0], xy[1])
        graham.add(point)
        jarvis.add(point)
    print("Convex Hull:", graham.get_hull_points())
    graham.display()
    print("Convex Hull:", jarvis.get_hull_points())
    jarvis.display()


def hull_data_set():
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
        points.append(Point(x, y))
    return points


def triangle_data_set():
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
        points.append(Point(s, t))
    return points


def main():
    # square_data_set()
    circle_data_set()


if __name__ == "__main__":
    main()
