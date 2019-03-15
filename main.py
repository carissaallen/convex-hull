from time import time

from datasets import square_data_set, circle_data_set, triangle_data_set, hull_data_set
import graham_scan
import jarvis_march


def run_graham_scan(dataset, size, show_progress):
    graham = graham_scan.GrahamScan()
    if dataset == 1:
        square_data_set(graham, size)
    elif dataset == 2:
        circle_data_set(graham, size)
    elif dataset == 3:
        triangle_data_set(graham, size)
    elif dataset == 4:
        hull_data_set(graham, size)
    else:
        square_data_set(graham, size)
    print("Convex Hull:", graham.get_hull_points(show_progress))
    graham.display()


def run_jarvis_march(dataset, size, show_progress):
    jarvis = jarvis_march.JarvisMarch()
    if dataset == 1:
        square_data_set(jarvis, size)
    elif dataset == 2:
        circle_data_set(jarvis, size)
    elif dataset == 3:
        triangle_data_set(jarvis, size)
    elif dataset == 4:
        hull_data_set(jarvis, size)
    else:
        square_data_set(jarvis, size)
    print("Convex Hull:", jarvis.get_hull_points(show_progress))
    jarvis.display()


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
    run_graham_scan(normal_dataset, input_size, show_progress)
    run_jarvis_march(normal_dataset, input_size, show_progress)


if __name__ == "__main__":
    main()
