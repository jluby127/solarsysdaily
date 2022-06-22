# SysView
# plotting functions
import matplotlib.pyplot as pt
import matplotlib as mpl
import numpy as np


def plotAll(allplanets, date):

    '''
    The main plotting function. Formatted the same each time, this displays the relative positions of all the planets at the user inputted timestamp.

    Inputs:
        - allplanets (list of dictionaries) - Each planet gets a dictionary with its relevant information (JD, RA, DEC, RANGE),
                                              and each dictionary is stored in this list.
        - date (string) - the user inputted date in question. Formatted as "YYYY-MM-DD".
    Outupts:
        - None.
    '''
    pt.rcParams['axes.facecolor']='gray'
    fig, ax = pt.subplots(figsize=(12,12))
    size = 32
    size2 = 15
    size3 = 8

    pt.xlim(-size, size)
    pt.ylim(-size, size)
    pt.xlabel("AU", fontsize=size2)
    pt.ylabel("AU", fontsize=size2)
    pt.tick_params(axis='both', labelsize=size2)
    cols = ['gray', 'darkorange', 'b', 'r', 'darkorange', 'yellow', 'c', 'b']

    pt.plot(0,0, marker='*', color='yellow', markeredgecolor='yellow', markersize=size3)

    for i in range(len(allplanets)):
        pt.plot(allplanets[i]['RANGE']*np.cos(allplanets[i]['RA']), allplanets[i]['RANGE']*np.sin(allplanets[i]['RA']), marker='o', color=cols[i], markeredgecolor='k', markersize=size3)
        pt.plot([0,allplanets[i]['RANGE']*np.cos(allplanets[i]['RA'])], [0, allplanets[i]['RANGE']*np.sin(allplanets[i]['RA'])], marker='o', color=cols[i], markeredgecolor='k', markersize=0, linestyle='-')

    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[0]['RANGE'], ec=cols[0], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[1]['RANGE'], ec=cols[1], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[2]['RANGE'], ec=cols[2], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[3]['RANGE'], ec=cols[3], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[4]['RANGE'], ec=cols[4], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[5]['RANGE'], ec=cols[5], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[6]['RANGE'], ec=cols[6], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[7]['RANGE'], ec=cols[7], fill=False))


    pt.annotate(date, xy=(-5.8,-5.8), fontsize=size2)
    pt.show()
