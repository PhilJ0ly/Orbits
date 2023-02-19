import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import textwrap
import argparse

planets = [
    "mercury",
    "venus",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "sun"
]
colors = ["red", "green", "blue", "orange", "purple", "brown", "pink", "yellow"]

def movingPlot(i, n, col):
    axis = plt.figure().add_subplot(projection='3d')
    df = pd.read_csv(f'../CleanData/{i}.csv')

    decArr, raArr, r = df['dec'].values, df['RA'].values, df['dist'].values
    decArr, raArr, r = df['dec'].values[:n], df['RA'].values[:n], df['dist'].values[:n]


    x = r*np.cos(raArr*np.pi/180)*np.cos(decArr*np.pi/180)
    y = r*np.sin(raArr*np.pi/180)*np.cos(decArr*np.pi/180)
    z = r*np.sin(decArr*np.pi/180)
    line = axis.plot([], [], [], label='parametric curve')[0]

    def update(i):
        line.set_data_3d(x[:i+2], y[:i+2], z[:i+2])
        line.set_color(col)
        return line

    axis.legend()
    ani = animation.FuncAnimation(axis.get_figure(), update, frames=len(x)-1, interval=100, blit=False)

    plt.show()

def plotAll(n):
    axis = plt.figure().add_subplot(projection='3d')
    for index, i in enumerate(planets):
        df = pd.read_csv(f'../CleanData/{i}.csv')
        decArr, raArr, r = df['dec'].values[:n], df['RA'].values[:n], df['dist'].values[:n]
        # decArr, raArr, r = df['dec'].values, df['RA'].values, df['dist'].values
        info = [r*np.cos(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(decArr*np.pi/180)]
        axis.plot(info[0], info[1], info[2], label=i, color=colors[index])
    axis.scatter(np.array([0]), np.array([0]), np.array(
        [0]), label='Earth', color='LightCoral')
    axis.legend()
    plt.show()


def plotAllSun(n):
    axis = plt.figure().add_subplot(projection='3d')
    dfSun = pd.read_csv(f'../CleanData/sun.csv')
    decArrSun, raArrSun, rSun = dfSun['dec'].values[:n], dfSun['RA'].values[:n], dfSun['dist'].values[:n]
    # decArrSun, raArrSun, rSun = df['dec'].values, df['RA'].values, df['dist'].values
    infoSun = [rSun*np.cos(raArrSun*np.pi/180)*np.cos(decArrSun*np.pi/180), rSun*np.sin(raArrSun*np.pi/180)*np.cos(decArrSun*np.pi/180), rSun*np.sin(decArrSun*np.pi/180)]
    for index, i in enumerate(planets):
        lbl = i
        if i != 'sun':
            df = pd.read_csv(f'../CleanData/{i}.csv')
            decArr, raArr, r = df['dec'].values[:n], df['RA'].values[:n], df['dist'].values[:n]
            # decArr, raArr, r = df['dec'].values, df['RA'].values, df['dist'].values
            info = [r*np.cos(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(decArr*np.pi/180)]
        else:
            info = [0, 0, 0]
            lbl= 'Earth'
        axis.plot(info[0]-infoSun[0], info[1]-infoSun[1], info[2]-infoSun[2], label=lbl, color=colors[index])
    axis.scatter(np.array([0]), np.array([0]), np.array(
        [0]), label='Sun', color='LightCoral')
    axis.legend()
    plt.show()

def plotSun(i, n, col):
    if i == 'sun':
        print('choose planet')
        return
    axis = plt.figure().add_subplot(projection='3d')
    dfSun = pd.read_csv(f'../CleanData/sun.csv')
    decArrSun, raArrSun, rSun = dfSun['dec'].values[:n], dfSun['RA'].values[:n], dfSun['dist'].values[:n]
    # decArrSun, raArrSun, rSun = df['dec'].values, df['RA'].values, df['dist'].values
    infoSun = [rSun*np.cos(raArrSun*np.pi/180)*np.cos(decArrSun*np.pi/180), rSun*np.sin(raArrSun*np.pi/180)*np.cos(decArrSun*np.pi/180), rSun*np.sin(decArrSun*np.pi/180)]
    lbl = i
    if i != 'earth':
        df = pd.read_csv(f'../CleanData/{i}.csv')
        decArr, raArr, r = df['dec'].values[:n], df['RA'].values[:n], df['dist'].values[:n]
        # decArr, raArr, r = df['dec'].values, df['RA'].values, df['dist'].values
        info = [r*np.cos(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(decArr*np.pi/180)]
    else:
        info = [0, 0, 0]
        lbl= 'earth'
    axis.plot(info[0]-infoSun[0], info[1]-infoSun[1], info[2]-infoSun[2], label=lbl, color=col)
    axis.scatter(np.array([0]), np.array([0]), np.array(
        [0]), label='Sun', color='LightCoral')
    axis.legend()
    plt.show()


def plot(i, n, col):
    axis = plt.figure().add_subplot(projection='3d')
    df = pd.read_csv(f'../CleanData/{i}.csv')

    decArr, raArr, r = df['dec'].values[:n], df['RA'].values[:n], df['dist'].values[:n]
    # decArr, raArr, r = df['dec'].values, df['RA'].values, df['dist'].values
    info = [r*np.cos(raArr*np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(raArr *np.pi/180)*np.cos(decArr*np.pi/180), r*np.sin(decArr*np.pi/180)]

    # trace orbit
    axis.plot(info[0], info[1], info[2], label=i, color=col)

    # earth
    axis.scatter(np.array([0]), np.array([0]), np.array([0]), label='Earth', color='LightCoral')

    # equator
    maxX = np.max(info[0])
    maxY = np.max(info[1])
    eqx = np.arange(-maxX, maxX, maxX/10)
    eqy = np.arange(-maxY, maxY, maxY/10)
    eqX, eqY = np.meshgrid(eqx, eqy)
    eqZ = np.zeros((len(eqx), len(eqy)))
    axis.plot_surface(eqX, eqY, eqZ, alpha=0.2)

    # vernal equinox
    vernX = np.arange(0, maxX, maxX/10)
    vernY, vernZ = np.zeros_like(vernX), np.zeros_like(vernX)
    axis.plot(vernX, vernY, vernZ, label="Vernal Equinox", color='black')

    x_label = 'Distance Parallel to the Celestial Equator and Vernal Equinox [AU]'
    y_label = 'Distance Parallel to the Celestial Equator and Perpendicular to the Vernal Equinox [AU]'
    z_label = 'Distance Perpendicular to the Celestial Equator and Vernal Equinox [AU]'
    axis.set_xlabel('\n'.join(textwrap.wrap(x_label, 20)), fontsize=6, labelpad=15, linespacing=1.5)
    axis.set_ylabel('\n'.join(textwrap.wrap(y_label, 20)), fontsize=6, labelpad=15, linespacing=1.5)
    axis.set_zlabel('\n'.join(textwrap.wrap(z_label, 20)), fontsize=6, labelpad=15, linespacing=1.5)
    axis.legend()
    plt.show()

def func(center, plt, n):
    if center == 'geo':
        if plt == 'all':
            plotAll(n)
        elif plt not in planets:
            print('incorrect planet entry')
            return    
        else:
            plot(plt, n, 'blue')
    else:
        if plt == 'all':
            plotAllSun(n)
        elif plt not in planets or plt == 'sun':
            if plt != 'earth':
                print('incorrect planet entry')
                return
        else:
            plotSun(plt, n, 'blue')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=str, help='geo/helio')
    parser.add_argument('arg2', type=str, help='planet/all')
    parser.add_argument('arg3', type=int, help='number of weeks')
    args = parser.parse_args()
    func(args.arg1, args.arg2, args.arg3)
