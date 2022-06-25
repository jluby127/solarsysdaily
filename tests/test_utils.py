# temp

import pytest
import solarsysdaily

from solarsysdaily import utils

def test_june242022():
    date = '2022-06-24'
    info = utils.gen_ephem_today(date)
    thetas = utils.coscalc(info)
    return info, thetas