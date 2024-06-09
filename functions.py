import numpy as np


def average(list):
    average = round(np.mean(list), 1)
    return average


def stdev(list):
    stdev = round(np.std(list), 1)
    return stdev
