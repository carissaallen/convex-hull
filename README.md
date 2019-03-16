# Convex Hull

## Project Requirements
Final research project for the graduate-level class, Algorithm Design and Analysis. 
* The topic should be related to algorithm complexity and must involve implementing one or more algorithms or data structures.
* After completing their research, students are responsible for writing a 7-10 page paper which is to be submitted along with their source code.

## Topic
Implement convex hull algorithms, which will include:
* Graham's scan
* Jarvis's March (Gift-Wrapping)

To implement in future work:
* _Divide-and-conquer_
* _Prune-and-search_
* _Chan's algorithm_

Compare the performance of each algorithm implemented, and create some visual representation (i.e. scatter plots) of the algorithms/performance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things were needed to set up the development environment and how to install them.
_Note: installation instructions based on macOS Mojave._

* [Python 3.7.2](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [matplotlib](https://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot)

Install pip:
```
curl https://bootstrap.pypa.io/gpython get-pip.pyet-pip.py -o get-pip.py
```
```
python get-pip.py
```

Install matplotlib:
```
pip install matplotlib
``` 

### Run

After installing any prerequisites listed above, follow these steps to run the program:

1. Clone the project to your local machine.<br>

    `git clone https://github.com/carissaallen/convex-hull.git`

2. From your terminal, enter the following command: <br>

    `python main.py`

### Hull Construction

To view the construction of the convex hull:
* Naviate to the _main.py_ file. In the `main` method:
* If `show_progress = False` then the scatter plot will only display the final convex hull boundary.
* If `show_progress = True` then the scatter plot will show the hull's progress as the boundary is constructed. <br>

  _Note: keep the input size small, this is pretty slow._ :turtle: 

## Tree
```bash
├── LICENSE
├── README.md
├── datasets.py
├── graham_scan.py
├── jarvis_march.py
├── main.py
└── scatter_plot.py
```

## Authors

* **Carissa Allen** - *Initial work* - [Convex Hull](https://github.com/carissaallen/convex-hull)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
A thank you to the individuals who created material I was able to use for inspiration, understanding and implementing technical details, and credit to any other resources that contributed to the making of my project. 👏🏻

* _Introduction to Algorithms 3rd Edition_ by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein
* Brian Faure for creating a [tutorial](https://steemit.com/python/@bfaure/graham-scan-algorithm-background-and-python-code) for Graham's Scan, which was used to learn about `matplotlib` to create the visual representation of the convex hull, and for some implementation details.
* [Determining if two consecutive line segments turn left or right](https://algorithmtutor.com/Computational-Geometry/Determining-if-two-consecutive-segments-turn-left-or-right/)
* [Convex Hull Algorithms: Jarvis's March](https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Jarvis-s-March/)
* [Computational Geometry Lecture](http://jeffe.cs.illinois.edu/teaching/compgeom/notes/01-convexhull.pdf) by Jeff Erickson
* [Computing Convex Hull in Python](https://startupnextdoor.com/computing-convex-hull-in-python/) by John Washam
* [Convex-Hull Algorithms](https://www.researchgate.net/publication/329265407_Convex-Hull_Algorithms_Implementation_Testing_and_Experimentation) by Neve Gamby and Jyrki Katajainen, primarily relied on to develop appropriate data sets as input to the algorithms implemented.
* To brush up on my geometry, [Text Computational Geometry in C](http://crtl-i.com/PDF/comp_c.pdf) by Joseph O'Rourke.
* [Convex Hull Applications](https://www.quora.com/What-are-the-real-life-applications-of-convex-hulls)
* [Spatial Extent of an Outbreak in Animal Epidemics](https://www.pnas.org/content/110/11/4239.full)
* [Hand Gesture Recognition Based on Convex Defect Detection](https://pdfs.semanticscholar.org/ee87/b0b46ed7a31ef90ee672c08a22e028e4537c.pdf)
* [The Convex Hull of a Finite Planar Set](http://www.math.ucsd.edu/~ronspubs/72_10_convex_hull.pdf) by R.L. Graham (1972)
