from matplotlib import pyplot as plot
from random import randint as rand


def scatter_plot(coordinates, convex_hull=None, color="m", title="Convex Hull"):
    """Given a list of (x,y) coordinates, creates a scatter plot.
    The convex_hull is the list of (x,y) coordinates that make up the convex hull."""
    xs, ys = zip(*coordinates)  # zip(*iterables): unzips into x and y coordinate lists
    plot.scatter(xs, ys, marker=".", linestyle="None")
    plot.title(title)

    if convex_hull != None:
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull):
                i = 0  # wrap the boundary line around
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plot.plot((c0[0], c1[0]), (c0[1], c1[1]), color)
        plot.show()


def draw_scatter_plot(coordinates, convex_hull=None, color="m", title="Convex Hull"):
    """Given a list of (x,y) coordinates, creates a scatter plot.
    The convex_hull is the list of (x,y) coordinates that make up the convex hull."""
    xs, ys = zip(*coordinates)  # zip(*iterables): unzips into x and y coordinate lists
    plot.scatter(xs, ys, marker=".", linestyle="None")
    plot.title(title)

    plot.ion()
    plot.draw()
    if convex_hull != None:
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull):
                i = 0  # wrap the boundary line around
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plot.plot((c0[0], c1[0]), (c0[1], c1[1]), color, linewidth=0.7)
            plot.pause(0.1)
    plot.show()
