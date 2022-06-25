# solsysdaily- A Solar System Viewing Tool.
[![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)

Team project from CodeAstro22 (Team #39): Visualizing the solar system at any given time.<br/>
With only a calendar date input as a string in the format YYYY-MM-DD, you can generate a top down view of our Solar System on that day, which shows the the arrangement of the planets around the Sun. It is intended to be a simple, educational tool.</br>

A future version will include an animation to show how the planets have moved/will move over one Earth year from the given date, and a random history fact for the day entered (since this is random, it may be an event that may not have happened before the year you entered)

## How to install:
```
pip install solarsysdaily
```

## How to use:
In a python file or jupyter notebook:
```
import solarsysdaily #this will generate a secret message
from solarsysdaily import utils
from solarsysdaily import plotting
date = "2000-01-01" #this is just an example date
planetdata = utils.gen_ephem_today(date)
angles = utils.coscalc(planetdata)
plotting.plotAll(planetdata, angles, truedist=False)
```

A plot window will launch, enjoy!

Detailed documentation can be found [here](https://solar-system-viewer.readthedocs.io/en/latest/).



