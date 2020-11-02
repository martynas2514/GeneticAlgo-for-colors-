import random
import math 
from itertools import product
import statistics 


def fitness(x, y):
    val = 0
    for i in range(len(x)):
        val += math.pow(x[i] - y[i], 2)
    return val

def addRandom(x ,coefR, min, max):
    # random number will be normally distributed over mean of the parents with std of 4
    if random.random() < coefR:
        mean = statistics.mean(x)
        randomn = random.gauss(mean,4)
        if randomn < min:
            randomn = min
        elif randomn > max:
            randomn = max
        else:
            randomn = math.floor(randomn)
        x.append(randomn)
    return x

def getBest(list, color, n):
    ctouples = []
    fit = [fitness(list[i], color) for i in range(len(list))]
    for i in range(n):
        a = fit.index(min(fit))
        ctouples.append(list[a])
        fit.pop(a)
    return ctouples

def newGen(parents, n, rand):
    #  crossover and mutation for every color

    arrG1 = addRandom([parents[i][0] for i in range(len(parents))], rand, 0, 255)
    arrG2 = addRandom([parents[i][1] for i in range(len(parents))], rand, 0, 255)
    arrG3 = addRandom([parents[i][2] for i in range(len(parents))], rand, 0, 255)
    crossover = product(arrG1, arrG2, arrG3)
    sampling = random.choices(list(crossover), k= n)
    return sampling

def colorGen(color, n, rand):
    #setting random color
    colors = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(10)]

    # fitting
    for i in range(n):
        a = getBest(colors, color, 2)
        colors = newGen(a, 10, rand)

    #taking best color 
    final = getBest(colors, color, 1)[0]
    fit = fitness(final, color)
    print("Color:", final, "SSE:", fit, sep= " ")

color = (10,10,10)
colorGen(color, 500, 0.2)

