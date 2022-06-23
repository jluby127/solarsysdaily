# SysView
# plotting functions
import matplotlib.pyplot as pt
import matplotlib as mpl
import numpy as np
pt.rcParams['axes.facecolor']='k'


def plotAll(allplanets, date, truedist=True):

    '''
    The main plotting function. Formatted the same each time, this displays the relative positions of all the planets at the user inputted timestamp.

    Inputs:
        - allplanets (list of dictionaries) - Each planet gets a dictionary with its relevant information (JD, RA, DEC, RANGE),
                                              and each dictionary is stored in this list.
        - date (string) - the user inputted date in question. Formatted as "YYYY-MM-DD".
        - truedist (boolean) - True if you want to see the true relative distances to the planets on the planet.
                               False if you want an evenly spaced system,
    Outupts:
        - None.
    '''
    pt.rcParams['axes.facecolor']='gray'
    fig, ax = pt.subplots(figsize=(12,12))
    size2 = 15
    size3 = 8
    pt.xlabel("AU", fontsize=size2)
    pt.ylabel("AU", fontsize=size2)
    pt.tick_params(axis='both', labelsize=size2)
    cols = ['gray', 'darkorange', 'b', 'r', 'darkorange', 'yellow', 'c', 'b']

    pt.plot(0,0, marker='*', color='yellow', markeredgecolor='yellow', markersize=size3*2, zorder=3)


    if truedist:
        audist = 32
        for i in range(len(allplanets)):
            pt.plot((allplanets[i]['HELRANGE']*np.cos(allplanets[i]['RA'])), (allplanets[i]['HELRANGE']*np.sin(allplanets[i]['RA'])), marker='o', color=cols[i], markeredgecolor='k', markersize=size3)
            pt.plot([0,(allplanets[i]['HELRANGE']*np.cos(allplanets[i]['RA']))], [0, (allplanets[i]['HELRANGE']*np.sin(allplanets[i]['RA']))], marker='o', color=cols[i], markeredgecolor='k', markersize=0, linestyle='-')
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[0]['HELRANGE'], ec=cols[0], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[1]['HELRANGE'], ec=cols[1], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[2]['HELRANGE'], ec=cols[2], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[3]['HELRANGE'], ec=cols[3], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[4]['HELRANGE'], ec=cols[4], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[5]['HELRANGE'], ec=cols[5], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[6]['HELRANGE'], ec=cols[6], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[7]['HELRANGE'], ec=cols[7], fill=False))

    else:
        audist = 9
        for i in range(len(allplanets)):
            pt.plot((i+1)*np.cos(allplanets[i]['RA']), (i+1)*np.sin(allplanets[i]['RA']), marker='o', color=cols[i], markeredgecolor='k', markersize=size3)
            pt.plot([0,(i+1)*np.cos(allplanets[i]['RA'])], [0, (i+1)*np.sin(allplanets[i]['RA'])], marker='o', color=cols[i], markeredgecolor='k', markersize=0, linestyle='-')
        ax.add_patch(mpl.patches.Circle((0, 0), radius=1, ec=cols[0], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=2, ec=cols[1], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=3, ec=cols[2], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=4, ec=cols[3], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=5, ec=cols[4], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=6, ec=cols[5], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=7, ec=cols[6], fill=False))
        ax.add_patch(mpl.patches.Circle((0, 0), radius=8, ec=cols[7], fill=False))

    ax.set_facecolor('k')

    pt.xlim(-audist, audist)
    pt.ylim(-audist, audist)

    pt.title(date, fontsize=size2*2)
    pt.show()


def plotinner(allplanets, date):

    '''
    Only plot the inner 5 planets

    Inputs:
        - allplanets (list of dictionaries) - Each planet gets a dictionary with its relevant information (JD, RA, DEC, RANGE),
                                              and each dictionary is stored in this list.
        - date (string) - the user inputted date in question. Formatted as "YYYY-MM-DD".
        - truedist (boolean) - True if you want to see the true relative distances to the planets on the planet.
                               False if you want an evenly spaced system,
    Outupts:
        - None.
    '''
    pt.rcParams['axes.facecolor']='gray'
    fig, ax = pt.subplots(figsize=(12,12))
    size2 = 15
    size3 = 8
    pt.xlabel("AU", fontsize=size2)
    pt.ylabel("AU", fontsize=size2)
    pt.tick_params(axis='both', labelsize=size2)
    cols = ['gray', 'darkorange', 'b', 'r', 'darkorange', 'yellow', 'c', 'b']

    pt.plot(0,0, marker='*', color='yellow', markeredgecolor='yellow', markersize=size3*2, zorder=3)

    audist = 6
    for i in range(len(allplanets)-3):
        pt.plot((allplanets[i]['RANGE']*np.cos(allplanets[i]['RA'])), (allplanets[i]['RANGE']*np.sin(allplanets[i]['RA'])), marker='o', color=cols[i], markeredgecolor='k', markersize=size3)
        pt.plot([0,(allplanets[i]['RANGE']*np.cos(allplanets[i]['RA']))], [0, (allplanets[i]['RANGE']*np.sin(allplanets[i]['RA']))], marker='o', color=cols[i], markeredgecolor='k', markersize=0, linestyle='-')
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[0]['RANGE'], ec=cols[0], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[1]['RANGE'], ec=cols[1], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[2]['RANGE'], ec=cols[2], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[3]['RANGE'], ec=cols[3], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[4]['RANGE'], ec=cols[4], fill=False))

    ax.set_facecolor('k')

    pt.xlim(-audist, audist)
    pt.ylim(-audist, audist)

    pt.title(date, fontsize=size2*2)
    pt.show()


def plotouter(allplanets, date):

    '''
    Only plot the outer 5 planets

    Inputs:
        - allplanets (list of dictionaries) - Each planet gets a dictionary with its relevant information (JD, RA, DEC, RANGE),
                                              and each dictionary is stored in this list.
        - date (string) - the user inputted date in question. Formatted as "YYYY-MM-DD".
    Outupts:
        - None.
    '''
    pt.rcParams['axes.facecolor']='gray'
    fig, ax = pt.subplots(figsize=(12,12))
    size2 = 15
    size3 = 8
    pt.xlabel("AU", fontsize=size2)
    pt.ylabel("AU", fontsize=size2)
    pt.tick_params(axis='both', labelsize=size2)
    cols = ['gray', 'darkorange', 'b', 'r', 'darkorange', 'yellow', 'c', 'b']

    pt.plot(0,0, marker='*', color='yellow', markeredgecolor='yellow', markersize=size3*2, zorder=3)

    audist = 32
    for i in range(3, len(allplanets)):
        pt.plot((allplanets[i]['RANGE']*np.cos(allplanets[i]['RA'])), (allplanets[i]['RANGE']*np.sin(allplanets[i]['RA'])), marker='o', color=cols[i], markeredgecolor='k', markersize=size3)
        pt.plot([0,(allplanets[i]['RANGE']*np.cos(allplanets[i]['RA']))], [0, (allplanets[i]['RANGE']*np.sin(allplanets[i]['RA']))], marker='o', color=cols[i], markeredgecolor='k', markersize=0, linestyle='-')
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[3]['RANGE'], ec=cols[3], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[4]['RANGE'], ec=cols[4], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[5]['RANGE'], ec=cols[5], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[6]['RANGE'], ec=cols[6], fill=False))
    ax.add_patch(mpl.patches.Circle((0, 0), radius=allplanets[7]['RANGE'], ec=cols[7], fill=False))

    ax.set_facecolor('k')

    pt.xlim(-audist, audist)
    pt.ylim(-audist, audist)

    pt.title(date, fontsize=size2*2)
    pt.show()
