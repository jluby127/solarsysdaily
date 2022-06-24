# Solar System Viewer
Team project from CodeAstro22 (Team #39): Visualizing the solar system at any given time.
With only a calendar date input in format YYYY-MM-DD, we will show you a top down view of our Solar System on that day, highlight the arrangement of the planets.

# How to install:
pip install solarsysdaily

# How to use:
In a python file or jupyter notebook:

from solarsysdaily import utils \n
from solarsysdaily import plotting \n
date = "2000-01-01" \n
planetdata = utils.gen_ephem_today(date) \n
angles = utils.coscalc(planetdata) \n
plotting.plotAll(planetdata, angles, truedist=False) \n

A plot window will launch, enjoy!
