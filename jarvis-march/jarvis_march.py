#!/usr/bin/env python3
"""
Jarvis's March Algorithm:
Finds the points in the convex hull by identifying the leftmost point,
and adding it to the hull at each iteration. This algorithm resembles selection sort.
1. Given a set of points, select the point with the smallest x-coordinate; 
   this is the leftmost point l, and is guaranteed to be a convex hull vertex.
   Add this point to the list of convex hull vertices.
2. Starting from l, the next vertex is the point p that creates the largest 
   right-hand turn from l. Now, if q is the vertex following p, and r is any
   other input point, then p,q,r must create the largest interior angle in 
   counterclockwise order. We must test each point to determine which one makes
   the largest right-hand turn, and then add it to the list of convex hull vertices. 
3. At this point, p becomes l, and we repeat Step 2 until we reach the
   initial starting point. 
"""
from matplotlib import pyplot as plot
from random import randint
from collections import namedtuple
from operator import itemgetter
from time import time
import sys

# adds higher directory to python modules path
sys.path.append("..")
from shared.scatter_plot import scatter_plot, seed

Point = namedtuple("Point", "x y")


class ConvexHull(object):
    points = []
    hull_points = []

    def __init__(self):
        pass

    def add(self, point):
        self.points.append(point)

    def get_orientation(self, origin, p1, p2):
        """Returns the orientation of point p1 relative to point p2 using origin.
        Returns a negative value if p1 follows p2 in 'clockwise' direction."""
        difference = ((p2.x - origin.x) * (p1.y - origin.y)) - (
            (p1.x - origin.x) * (p2.y - origin.y)
        )
        return difference

    def jarvis_march(self, show_hull_construction=False):
        """Computes the points that make up the convex hull."""
        points = self.points

        # get leftmost point
        start = min(points, key=itemgetter(0))
        point = start
        self.hull_points.append(start)

        far_point = None
        while far_point is not start:
            p1 = None
            for p in points:
                if p is point:
                    continue
                else:
                    p1 = p
                    break
            far_point = p1

            for p2 in points:
                # do not compare to self or pivot point
                if p2 is point or p2 is p1:
                    continue
                else:
                    direction = self.get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2
            self.hull_points.append(far_point)
            point = far_point
            if show_hull_construction:
                scatter_plot(self.points, self.hull_points)

    def get_hull_points(self):
        if self.points and not self.hull_points:
            self.jarvis_march(True)
        return self.hull_points

    def display(self):
        # all points
        x = [p.x for p in self.points]
        y = [p.y for p in self.points]
        plot.plot(x, y, marker="D", linestyle="None")

        # hull points
        hx = [p.x for p in self.hull_points]
        hy = [p.y for p in self.hull_points]
        plot.plot(hx, hy)

        plot.title("Convex Hull")
        plot.show()


def benchmark(sizes=[10, 100, 1000, 10000, 100000]):
    """Created as a performance metric."""
    pass


def main():
    ch = ConvexHull()
    for _ in range(50):
        ch.add(Point(randint(-100, 100), randint(-100, 100)))

    print("Covex Hull:", ch.get_hull_points())
    ch.display()


if __name__ == "__main__":
    main()
