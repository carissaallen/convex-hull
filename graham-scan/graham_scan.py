#!/usr/bin/env python3
"""
Graham's Scan Algorithm: 
1. Choose point p with the lowest y-coordinate; in case of a tie,
   choose the leftmost point. Since no point is below p, it must
   be a vertex on the convex hull. (This is our 'anchor' point.)
2. Sort the remaining points in order of increasing polar angle from p.
   If two or more points have the same polar angle, choose the farthest point.
3. Initialize the stack with anchor point p and the first element in the 
   sorted list.
4. Iterate over each point in the sorted list; each time we find a vertex
   at which we make a nonleft (CW) turn, pop the vertex from the stack (i.e.,
   remove from the convex hull). (Note: by checking for a nonleft turn instead of a right turn, 
   this test precludes the possibility of a straiht angle at a vertex.) After popping all
   vertices that have nonleft turns when heading toward point p, push p on to the stack.
"""
from matplotlib import pyplot as plot
from random import randint
from math import atan2
from time import time

from scatter_plot import scatter_plot, seed


def quicksort(set_of_points):
    """Sorts the set of points in order of increasing polar angle from the anchor point."""
    if len(set_of_points) <= 1:
        return set_of_points
    smaller, equal, larger = [], [], []
    pivot_angle = polar_angle(set_of_points[randint(0, len(set_of_points) - 1)]) # select random pivot
    for p in set_of_points:
        angle = polar_angle(p) # calculate current angle
        if angle < pivot_angle: smaller.append(p)
        elif angle == pivot_angle: equal.append(p)
        else: larger.append(p)
    return quicksort(smaller) + sorted(equal, key=distance) + quicksort(larger)


def polar_angle(p0, p1=None):
    """Returns the polar angle (in radians) from points p0 to p1."""
    if p1 == None:
        p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return atan2(y_span, x_span)


def distance(p0, p1=None):
    """Returns the eculidean distance from p0 to p1."""
    if p1 == None:
        p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return y_span ** 2 + x_span ** 2


def rotation(p1, p2, p3):
    """Returns the rotation direction. 

	If > 0, counter-clockwise.
	If < 0, clockwise. 
	If = 0, collinear."""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


def graham_scan(points, show_hull_construction=False):
    """Returns the vertices that lie on the convex hull.

	Input: a set of (x,y) coordinates. 
	Output: a set of (x,y) coordinates on the convex hull.
	When the 'show_hull_construction' flag is set to True, 
	the scatter plot will show the construction of the convex hull
	at each iteration."""
    global anchor  # point (x,y) with the smallest y value

    min_index = None
    for i, (x, y) in enumerate(points):
        if min_index == None or y < points[min_index][1]:
            min_index = i
        if y == points[min_index][1] and x < points[min_index][0]:
            min_index = i
    anchor = points[min_index]
    sorted_points = quicksort(points)
    del sorted_points[sorted_points.index(anchor)]
    # the 'anchor' point and the point with smallest polar angle will always be on hull
    hull = [anchor, sorted_points[0]]
    for s in sorted_points[1:]:
        while rotation(hull[-2], hull[-1], s) <= 0:
            del hull[-1] # backtrack
        hull.append(s)
        if show_hull_construction:
            scatter_plot(points, hull)
    return hull


def benchmark(sizes=[10, 100, 1000, 10000, 100000]):
    """Created as a performance metric."""
    for s in sizes:
        total_time = 0.0
        for _ in range(3):
            set_of_points = seed(s, 0, max(sizes) * 10)
            start_time = time()
            hull = graham_scan(set_of_points, False)
            total_time += time() - start_time
        print("size %d time: %0.5f" % (s, total_time / 3.0))


def main():
    set_of_points = seed(100)
    print("Points:", set_of_points)
    hull = graham_scan(set_of_points, False)
    print("Hull:", hull)
    scatter_plot(set_of_points, hull)


if __name__ == "__main__":
    main()
