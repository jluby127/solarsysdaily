# End to end test of solarsystemviewer
import sys
import os
sys.path.append("../solarsystemviewer/")
import utils as ut
import plotting as pt

def end2end(date):

    planetdata = ut.gen_ephem_today(date)
    angles = ut.coscalc(planetdata)

    pt.plotAll(planetdata, angles, truedist=True)
    pt.plotAll(planetdata, angles, truedist=False)
    pt.plotinner(planetdata, angles)
    pt.plotouter(planetdata, angles)


end2end("1963-11-22")
