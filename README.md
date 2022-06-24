# Solar System Viewer
Team project from CodeAstro22 (Team #39): Visualizing the solar system at any given time.<br/>
With only a calendar date input in format YYYY-MM-DD, we will show you a top down view of our Solar System on that day, highlight the arrangement of the planets.

# How to install:
pip install solarsysdaily

# How to use:
In a python file or jupyter notebook:

from solarsysdaily import utils<br/>
from solarsysdaily import plotting<br/>
date = "2000-01-01"<br/>
planetdata = utils.gen_ephem_today(date)<br/>
angles = utils.coscalc(planetdata)<br/>
plotting.plotAll(planetdata, angles, truedist=False)<br/>

A plot window will launch, enjoy!


[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
