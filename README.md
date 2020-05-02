# Swarm Robots Localisation Code

In addition to the MP Lab robot code in [Swarm Robots](https://github.com/JamieS1211/GroupSwarmRobots), this repository contains additional Python and Arduino Code. The majority of this code was produced for the localisation system.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Please run every python script in it's own directory.

### Software

* [Python](https://www.python.org/) - The main programming language used. 3.7 release was used for all python code. Check specific modules for compatibility.
* [Arduino](https://www.arduino.cc/en/main/software) - For interfacing between the UART from the robot microcontroller and the computer, an Arduino was used.

### Python Modules

Core modules like math, random, numpy etc... not included. You can either create a virtual environment in the directory or just install these modules to you python installation.

* [pandas](https://pandas.pydata.org/) - Dataframe creation.
* [matplotlib](https://matplotlib.org/) - Basic plotting.
* [seaborn](https://seaborn.pydata.org/) - More complex plotting.
* [SymPy](https://www.sympy.org/en/index.html) - Symbolic Python. Solving equations symbolically.
* [PySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html) - Allows Python to read Serial in.
* [opencv](https://pypi.org/project/opencv-python/) - Used for the object tracking and detection.
* [CamGear](https://github.com/abhiTronix/vidgear/wiki/CamGear) - Used to interact with live video streams.
* [pafy](https://pypi.org/project/pafy/) - Used to interact with youtube livestreams.

### Arduino Libraries

* [QMC5883L Compass](https://github.com/mprograms/QMC5883LCompass) - To save time a premade library for the compass was used for testing of accuracy. Also has good documentation.

## Authors

* **Will Rice** - 90% of the stuff
* **Oliver Poulter** - opencv, object detection and tracking code
* **Andrew Guest** - Battery data

## License

I don't understand licenses but this was made as part of a master's project for the University of Exeter, CEMPS. Probabl falls under some academic fair use thingy.

## Acknowledgments

* Dr Dibin Zhu (Project Supervisor)