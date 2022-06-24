# SysView
# utility functions
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os

def parsedata(filelist, date):
    """ Parse Data

    Read and parse the relevant data from the Horizons@JPL (https://ssd.jpl.nasa.gov/horizons/app.html#/) curl command

    Args:
        filelist (array of strings): an array where each element is the name of the file pulled from Horizons for the ith planet

    Returns:
        allplanets-- A list of dictionaries with each planet's relevant information [RA, DEC, HELRANGE (Sun-Planet distance), EARTHRANGE (Earth-Planet distance)],and each dictionary is stored in this list.
    Return Type:
        list
    """
    allplanets = []
    data = "temp holding string"

    for f in filelist:
        lines = []
        with open(f+'.csv','r') as dataFile:
            for line in dataFile:
                line = line.strip()
                lines.append(line)
        for i in range(len(lines)):
            if lines[i] == "$$SOE": # The data we are interested in is stored in csv format in the line after this keyword
                data = lines[i+1]
                break

        datastrip = data.split(',')
        dataformatted = []
        for d in datastrip:
            dataformatted.append(d)

        if f == 'earth':
            datadict = {"DATE":date,"RA":float(dataformatted[3]), "DEC":float(dataformatted[4]), "HELRANGE":float(dataformatted[7]), "EARTHRANGE":float(dataformatted[5])}
            allplanets.append(datadict)
        else:
            datadict = {"DATE":date,"RA":float(dataformatted[3]), "DEC":float(dataformatted[4]), "HELRANGE":float(dataformatted[5]), "EARTHRANGE":float(dataformatted[7])}
            allplanets.append(datadict)

    return allplanets

def gen_ephem_today(date):
    '''Ephemeris generator for given date

    Generates the equatorial coordinates and distance to a planet as observed from Earth, and its distance to the Sun.

    Args:
	    date (string): Date to view the Solar System in YYYY-MM-DD format

    Returns:
	    parseData(files)
    Return Type:
        list
    '''



    planets = [199,299,10,499,599,699,799,899]
    files = ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
    date_obs = date.split("-")
    yyyy,mm,dd = int(date_obs[0]),str(date_obs[1]),int(date_obs[2])
    if yyyy < 1 or yyyy > 9999:
        print("Invalid date: year must be between 1 and 9999")
        print("Returning \"None\" and stopping.")
        return None

    date_in = '{}-'.format(yyyy)+mm+'-{}'.format(dd)+' 00:01'
    date_next = '{}-'.format(yyyy)+mm+'-{}'.format(dd)+' 23:59'
    # year_next = '{}-'.format(y+1)+mm+'-{}'.format(d)


    for i in range(8):
        URL_pre = 'https://ssd.jpl.nasa.gov/api/horizons.api?format=text&'
        planet = 'COMMAND=\'{}\'&'.format(planets[i])
        ephem_setting = 'OBJ_DATA=\'YES\'&MAKE_EPHEM=\'YES\'&EPHEM_TYPE=\'OBSERVER\'&'
        obs = 'CENTER=\'50\'&'
        duration='START_TIME=\''+date_in+'\'&STOP_TIME=\''+date_next+'\'&STEP_SIZE=\'1%20d\'&'
        data = 'QUANTITIES=\'2,19,20\'&'
        ang = 'ANG_FORMAT=\'DEG\'&'
        csv_format = 'CSV_FORMAT=\'YES\''
        URL = str(URL_pre+planet+ephem_setting+obs+duration+data+ang+csv_format)
        r = requests.get(url = URL)
        data = r.content
        data = data.decode()
        type(data)
        f = open(files[i]+'.csv','w')
        f.write(data)
        f.close()

    return parsedata(files, date)



# PlanetDist = np.array([0.39, 0.72, 1, 1.52, 5.20, 9.58, 19.20, 30.05])
#Define cosine calculation function \n",
def coscalc(planetinfo):
    """ Cosine Angle Calculation

    Calculate the angle between earth-planet line and sun-planet line using cosine rules.

    Args:
        -planetinfo: Dictionary. The dictionary of ephemeris information from gen_ephem_today

    Returns:
        Listed of values of angle theta in radian
    Return type:
        list

    """
    theta_all = []
    for i in range(len(planetinfo)):
        if i == 2:
            theta = planetinfo[i]['RA']*(180/np.pi)
            theta_all.append(theta)
        else:
            ep = planetinfo[i]['EARTHRANGE']
            hp = planetinfo[i]['HELRANGE']
            costop = (ep**2-1-hp**2)
            cosbot = 2*hp
            if abs(costop/cosbot) > 1:
                print("Error with ratio for planet: " + str(i))
            theta = np.arccos(costop/cosbot)
            theta *= (180/np.pi)
            theta_all.append(theta)
    return theta_all


# def isUP(allplanets):
#     ups = []
#     for i in range(len(allplanets)):
#         print(allplanets[i]['RA'])
#         if i != 2:
#             if abs(allplanets[2]['RA'] - allplanets[i]['RA']) < 90:
#                 ups.append(1)
#             else:
#                 ups.append(0)
#         else:
#             ups.append(0)
#     print("Planets Above Horizon at Midnight: ")
#     names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#     for n in range(len(names)):
#         if ups[n] == 1:
#             print(names[n])
