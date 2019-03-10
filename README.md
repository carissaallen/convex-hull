# Convex Hull

## Project Requirements
Final research project for the graduate-level class, Algorithm Design and Analysis. 
* The topic should be related to algorithm complexity and must involve implementing one or more algorithms or data structures.
* After completing their research, students are responsible for writing a 7-10 page paper which is to be submitted along with their source code.

## Topic
Implement several convex hull algorithms, which will include:
* Graham's scan
* Jarvis's March (Gift-Wrapping) 
* _Divide-and-conquer_
* _Prune-and-search_

Compare the performance of each algorithm implemented, and create some visual representation (i.e. scatter plots) of the algorithms/performance.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things were needed to set up the development environment and how to install them.
_Note: installation instructions based on macOS Mojave_

* Python 3.7.2
* pip 
* matplotlib

Install [pip](https://pip.pypa.io/en/stable/installing/):
```
curl https://bootstrap.pypa.io/gpython get-pip.pyet-pip.py -o get-pip.py
```
```
python get-pip.py
```

Install [matplotlib](https://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot):
```
pip install matplotlib
``` 

## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

* **Carissa Allen** - *Initial work* - [Convex Hull](https://github.com/carissaallen/convex-hull)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
A thank you to the individuals who created material I was able to use for inspiration, understanding and implementing technical details, and credit to any other resources that contributed to the making of my project. :clap:

* Brian Faure for creating a [tutorial](https://steemit.com/python/@bfaure/graham-scan-algorithm-background-and-python-code) for Graham's Scan, which was used to learn about `matplotlib` to create the visual representation of the convex hull, and for some implementation details.
* [Determining if two consecutive line segments turn left or right](https://algorithmtutor.com/Computational-Geometry/Determining-if-two-consecutive-segments-turn-left-or-right/)
* [Convex Hull Algorithms: Jarvis's March](https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Jarvis-s-March/)
* [Computational Geometry Lecture](http://jeffe.cs.illinois.edu/teaching/compgeom/notes/01-convexhull.pdf) by Jeff Erickson
* [Computing Convex Hull in Python](https://startupnextdoor.com/computing-convex-hull-in-python/) by John Washam
* [Convex-Hull Algorithms](https://www.researchgate.net/publication/329265407_Convex-Hull_Algorithms_Implementation_Testing_and_Experimentation) by Neve Gamby and Jyrki Katajainen, primarily relied on to develop appropriate data sets as input to the algorithms implemented.
