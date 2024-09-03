import numpy as np


def solution_station_6(input):
    a = 0.9994
    b = 1.0004
    c = -0.0006
    d = 0.0006
    return a * np.sin(b * input + c) + d
