# SysView
# utility functions
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os

def parseData(filelist):
    '''
    We pull all data from Horizons@JPFL (https://ssd.jpl.nasa.gov/horizons/app.html#/) but this data file is poorly formatted.
    We use this function to extract only the data we are interested in, and in the format that works for us.

    Inputs:
        - filelist (list of strings) - a list of names for the files curled from Horizons which contain the information for each planet.
                                       Each planet gets its own file, so this list should always have len(filelist) = 8.
    Outputs:
        - allplanets (list of dictionaries) - Each planet gets a dictionary with its relevant information (JD, RA, DEC, RANGE),
                                              and each dictionary is stored in this list.
    '''
    allplanets = []

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

        datadict = {"RA":float(dataformatted[3]), "DEC":float(dataformatted[4]), "EARTHRANGE":float(dataformatted[5]), "HELRANGE":float(dataformatted[7])}
        allplanets.append(datadict)

    return allplanets

def gen_ephem_today(yyyy='2022',mm='06',dd='22'):
    '''
    Input: Year, Month and Day as strings
    Output: Ephemeris file for the day
    '''
    planets = [199,299,10,499,599,699,799,899]
    files = ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']

    date_in = '{}-'.format(int(yyyy))+mm+'-{}'.format(int(dd))
    date_next = '{}-'.format(int(yyyy))+mm+'-{}'.format(int(dd)+1)
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

    return parseData(files)


PlanetDist = np.array([0.39, 0.72, 1, 1.52, 5.20, 9.58, 19.20, 30.05])
#Define cosine calculation function \n",
def CosCalc(ep):
    costop = (np.sqrt(ep)-1-np.sqrt(PlanetDist))
    cosbot = 2* PlanetDist
    theta = np.arccos(costop/cosbot)
    return theta


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
