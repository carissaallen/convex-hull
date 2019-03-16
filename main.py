from time import time

from datasets import square, circle, triangle, hull
import graham_scan
import jarvis_march


def run_algorithms(dataset, size, show_progress):
    graham = graham_scan.GrahamScan()
    jarvis = jarvis_march.JarvisMarch()
    if dataset == 1:
        start = time()
        square(graham, size)
        total = (time() - start)
        print("Graham's scan execution time: {} seconds").format(total)
        start = time()
        square(jarvis, size)
        total = (time() - start)
        print("Jarvis's march execution time: {} seconds").format(total)
    elif dataset == 2:
        start = time()
        points = circle(graham, size)
        total = (time() - start)
        print("Graham's scan execution time: {} seconds").format(total)
        start = time()
        add(jarvis, points)
        total = (time() - start)
        print("Jarvis's march execution time: {} seconds").format(total)
    elif dataset == 3:
        start = time()
        points = triangle(graham, size)
        total = (time() - start)
        print("Graham's scan execution time: {} seconds").format(total)
        start = time()
        add(jarvis, points)
        total = (time() - start)
        print("Jarvis's march execution time: {} seconds").format(total)
    elif dataset == 4:
        start = time()
        points = hull(graham, size)
        total = (time() - start)
        print("Graham's scan execution time: {} seconds").format(total)
        add(jarvis, points)
        total = (time() - start)
        print("Jarvis's march execution time: {} seconds").format(total)
    else:
        square(graham, size)
        square(jarvis, size)
    print("Convex Hull:", graham.get_hull_points(show_progress))
    print("Convex Hull:", jarvis.get_hull_points(show_progress))
    graham.display()
    jarvis.display()


def add(algorithm, points):
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

    # run the algorithms (one at a time)
    run_algorithms(normal_dataset, input_size, show_progress)
    # run_algorithms(circle_dataset, input_size, show_progress)
    # run_algorithms(triangle_dataset, input_size, show_progress)
    # run_algorithms(hull_dataset, input_size, show_progress)


if __name__ == "__main__":
    main()
