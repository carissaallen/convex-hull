from time import time

from datasets import (
    square_data_set,
    circle_data_set,
    triangle_data_set,
    hull_data_set
)
import graham_scan
import jarvis_march


def run_algorithms(dataset, size, show_progress):
    graham = graham_scan.GrahamScan()
    jarvis = jarvis_march.JarvisMarch()
    if dataset == 1:
        square_data_set(graham, size)
        square_data_set(jarvis, size)
    elif dataset == 2:
        points = circle_data_set(graham, size)
        add_points(jarvis, points)
    elif dataset == 3:
        points = triangle_data_set(graham, size)
        add_points(jarvis, points)
    elif dataset == 4:
        points = hull_data_set(graham, size)
        add_points(jarvis, points)
    else:
        square_data_set(graham, size)
        square_data_set(jarvis, size)
    print("Convex Hull:", graham.get_hull_points(show_progress))
    print("Convex Hull:", jarvis.get_hull_points(show_progress))
    graham.display()
    jarvis.display()


def add_points(algorithm, points):
    for p in points:
        algorithm.add(p)


def main():

    # size of the set of input points
    input_size = 100

    # set to 'True' to display convex hull construction
    show_progress = False

    normal_dataset = 1  # points distributed over square-shaped interval
    circle_dataset = 2  # points distributed over circle-shaped interval
    triangle_dataset = 3  # points distributed over triangle-shaped interval
    hull_dataset = 4  # all points distributed on the hull

    # run the algorithms
    # run_algorithms(normal_dataset, input_size, show_progress)
    # run_algorithms(circle_dataset, input_size, show_progress)
    # run_algorithms(triangle_dataset, input_size, show_progress)
    # run_algorithms(hull_dataset, input_size, show_progress)


if __name__ == "__main__":
    main()
