# SysView
# utility functions
import numpy as np


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
        with open(f,'r') as dataFile:
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

        datadict = {"JD":dataformatted[0], "RA":float(dataformatted[3]), "DEC":float(dataformatted[4]), "RANGE":float(dataformatted[5])}
        allplanets.append(datadict)

    return allplanets




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
