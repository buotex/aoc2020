from collections import namedtuple
from dataclasses import dataclass
import numpy as np

@dataclass
class KeyLimits:
    min_i: int
    min_j: int
    max_i: int
    max_j: int


def get_limits(data):
    max_i = max(data.keys(), key=lambda x: x[0])[0]
    max_j = max(data.keys(), key=lambda x: x[1])[1]
    min_i = min(data.keys(), key=lambda x: x[0])[0]
    min_j = min(data.keys(), key=lambda x: x[1])[1]
    return KeyLimits(min_i, min_j, max_i, max_j)


def get_neighbors(key, full=True):
    my_key = np.array(key)
    neighbor1 = my_key + np.array((1,0))
    neighbor2 = my_key + np.array((0,1))
    neighbor3 = my_key + np.array((0,-1))
    neighbor4 = my_key + np.array((-1,0))
    neighbor5 = my_key + np.array((1,1))
    neighbor6 = my_key + np.array((-1,-1))
    neighbor7 = my_key + np.array((-1,1))
    neighbor8 = my_key + np.array((1,-1))
    neighbors = [neighbor1, neighbor2, neighbor3, neighbor4]
    if full == True:
        neighbors.extend([neighbor5, neighbor6, neighbor7, neighbor8])
    return neighbors


def get_directions(full = True):
    dir1 = (1,0)
    dir2 = (0,1)
    dir3 = (0,-1)
    dir4 = (-1,0)
    dir5 = (1,1)
    dir6 = (-1,-1)
    dir7= (-1,1)
    dir8 = (1,-1)
    if full == True:
        directions = [dir1, dir2, dir3, dir4, dir5, dir6, dir7, dir8]
    else:
        directions = [dir1, dir2, dir3, dir4]
    return [np.array(dir) for dir in directions]





    
