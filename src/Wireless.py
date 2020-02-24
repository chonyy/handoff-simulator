import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import random
import math
from carClass import car
from utils import changedirection, goDirection, go, carEnter, power, checkHandoff
import utils

carToRemove = []
cars = []
handOffPlotBest = []
handOffPlotT = []
handOffPlotE = []
handOffPlotM = []
carnum = 0

if __name__ == '__main__':
    for i in range(86400): #simulation starting here
        # print(i)
        carToRemove.clear()
        carEnter(cars)
        for drivingCar in cars:
            if (drivingCar.x < 0 or drivingCar.x > 3000 or drivingCar.y < 0 or drivingCar.y > 3000):
                carToRemove.append(drivingCar)
            else:
                checkHandoff(drivingCar)
                go(drivingCar)
        for toremove in carToRemove:
            cars.remove(toremove)
        handOffPlotBest.append(utils.handOffBest)
        handOffPlotT.append(utils.handOffT)
        handOffPlotE.append(utils.handOffE)
        handOffPlotM.append(utils.handOffM)
        carnum += len(cars)
        print(len(cars))

    print(len(cars))
    print("best: ", utils.handOffBest, "handoffs")
    print('avgPowerBest', utils.totalpowerB / carnum)
    print()
    print("threshold: ", utils.handOffT, "handoffs")
    print('avgPowerT', utils.totalpowerT / carnum)
    print()
    print("entrophy: ", utils.handOffE, "handoffs")
    print('avgPowerE', utils.totalpowerE / carnum)
    print()
    print("Minimum policy: ", utils.handOffM, "handoffs")
    print("avgPowerM", utils.totalpowerM / carnum)

    fig = plt.figure(1, figsize=(15, 7))
    gs = gridspec.GridSpec(1, 2, width_ratios=[3, 2])
    plt.subplot(gs[0])
    plt.plot(handOffPlotBest, label='Best', linewidth=6, alpha=0.6)
    plt.plot(handOffPlotT, label='Threshold', linewidth=6, alpha=0.6)
    plt.plot(handOffPlotE, label='Entrophy',linewidth=6, alpha=0.6)
    plt.plot(handOffPlotM, label='Minimum Own Policy', linewidth=6, alpha=0.6)
    plt.title('Handoffs of Differnet Policies')
    plt.xlabel('Second')
    plt.ylabel('Handoffs')
    plt.legend()
    plt.subplot(gs[1])
    plt.text(0.1, 0.9, 'Handoffs of Best Policy: {} times'.format(utils.handOffBest), fontsize=10)
    plt.text(0.1, 0.8, 'Handoffs of Threshold Policy: {} times'.format(utils.handOffT), fontsize=10)
    plt.text(0.1, 0.7, 'Handoff of Entrophy Policy: {} times'.format(utils.handOffE), fontsize=10)
    plt.text(0.1, 0.6, 'Handoffs of Minimum Policy: {} times'.format(utils.handOffM), fontsize=10)
    plt.text(0.1, 0.4, 'Average Power of Best Policy: {} dBm'.format(utils.totalpowerB / carnum), fontsize=10)
    plt.text(0.1, 0.3, 'Average Power of Threshold Policy: {} dBm'.format(utils.totalpowerT / carnum), fontsize=10)
    plt.text(0.1, 0.2, 'Average Power of Entrophy Policy: {} dBm'.format(utils.totalpowerE / carnum), fontsize=10)
    plt.text(0.1, 0.1, 'Average Power of Minimum Policy: {} dBm'.format(utils.totalpowerM / carnum), fontsize=10)
    plt.axis('off')
    plt.show()
