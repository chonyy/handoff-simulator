import random
from carClass import car
import math

speed = 10
pmin = -125
p = 0.03224053668
e = 5
t = -110
station = [(750,750), (2250, 750), (750, 2250), (2250, 2250)]
totalpowerB = 0
totalpowerT = 0
totalpowerE = 0
totalpowerM = 0
handOffBest = 0
handOffT = 0
handOffE = 0
handOffM = 0


def changedirection(car, orig):
    if(car.x % 3000 == 0 and car.y % 3000 == 0) :
        if(car.x == 0 and car.y == 0):
            if(orig == 0):
                orig = 1
            elif(orig == 3):
                orig = 2
        elif (car.x == 3000 and car.y == 0):
            if (orig == 1):
                orig = 2
            elif (orig == 0):
                orig = 3
        elif (car.x == 0 and car.y == 3000):
            if (orig == 2):
                orig = 1
            elif (orig == 3):
                orig = 0
        elif (car.x == 3000 and car.y == 3000):
            if (orig == 2):
                orig = 3
            elif (orig == 1):
                orig = 0
    else:
        randnum = random.randrange(6) + 1
        if(randnum == 1): #turn left
            orig = orig - 1
        elif(randnum == 2 or randnum == 3): #turn right
            orig = orig + 1

        if(orig == -1):
            orig = 3
        orig = orig % 4

    car.direction = orig

def goDirection(car, direction):
    if(direction == 0):
        car.y -= speed
    elif(direction == 1):
        car.x += speed
    elif(direction == 2):
        car.y += speed
    elif(direction == 3):
        car.x -= speed

def go(car):
    if(car.x % 750 == 0 and car.y % 750 == 0):
        changedirection(car, car.direction)
    goDirection(car, car.direction)

def carEnter(cars):
    for j in range(12):
        enter = random.random() < p
        if(j == 0): #from top left to clockwise
            if(enter):
                cars.append(car(750, 0, 2, 0, 0, 0, 0))
        elif (j == 1):
            if (enter):
                cars.append(car(1500, 0, 2, 0, 0, 0, 0))
        elif (j == 2):
            if (enter):
                cars.append(car(2250, 0, 2, 1, 1, 1, 1))
        elif (j == 3):
            if (enter):
                cars.append(car(3000, 750, 3, 1, 1, 1, 1))
        elif (j == 4):
            if (enter):
                cars.append(car(3000, 1500, 3, 1, 1, 1, 1))
        elif (j == 5):
            if (enter):
                cars.append(car(3000, 2250, 3, 3, 3, 3, 3))
        elif (j == 6):
            if (enter):
                cars.append(car(2250, 3000, 0, 3, 3, 3, 3))
        elif (j == 7):
            if (enter):
                cars.append(car(1500, 3000, 0, 3, 3, 3, 3))
        elif (j == 8):
            if (enter):
                cars.append(car(750, 3000, 0, 2, 2, 2, 2))
        elif (j == 9):
            if (enter):
                cars.append(car(0, 2250, 1, 2, 2, 2, 2))
        elif (j == 10):
            if (enter):
                cars.append(car(0, 1500, 1, 2, 2, 2, 2))
        elif (j == 11):
            if (enter):
                cars.append(car(0, 750, 1, 0, 0, 0, 0))

def power(car, station):
    xdiff = abs(car.x - station[0])
    ydiff = abs(car.y - station[1])
    dist = (xdiff ** 2 + ydiff ** 2) ** (1/2)
    if(dist == 0):
        return -50
    else:
        return -60 - 20 * math.log(dist, 10)

def checkHandoff(car):
    global handOffBest
    global handOffT
    global handOffE
    global handOffM
    global totalpowerB
    global totalpowerT
    global totalpowerE
    global totalpowerM

    powerRec = []
    powerRec.append(power(car, station[0]))
    powerRec.append(power(car, station[1]))
    powerRec.append(power(car, station[2]))
    powerRec.append(power(car, station[3]))
    pnew = max(powerRec)
    newservice = powerRec.index(max(powerRec))

    poldB = power(car, station[car.serviceB])
    poldT = power(car, station[car.serviceT])
    poldE = power(car, station[car.serviceE])
    poldO = power(car, station[car.serviceO])

    if(pnew > poldB): #best
        totalpowerB += pnew
        car.serviceB = newservice
        handOffBest += 1
    else:
        totalpowerB += poldB

    if(pnew > poldT and poldT < t): #threshold
        totalpowerT += pnew
        car.serviceT = newservice
        handOffT += 1
    else:
        totalpowerT += poldT

    if(pnew > poldE + e): #entrophy
        totalpowerE += pnew
        car.serviceE = newservice
        handOffE += 1
    else:
        totalpowerE += poldE

    if(poldO < pmin): #my own policy
        totalpowerM += pnew
        car.serviceO = newservice
        handOffM += 1
    else:
        totalpowerM += poldO