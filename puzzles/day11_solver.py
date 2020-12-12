import numpy as np  # noqa
import pandas as pd  # noqa
import io  # noqa
import re  # noqa
import sys  # noqa
import itertools  # noqa
import functools  # noqa


from loguru import logger
from pytest import fixture

import aoc
from aoc.pc import *  # noqa

from aoc.utils import get_limits

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def algo1(entry):
    new_entry = entry.copy()
    for key, value in entry.items():
        if value == -1:
            continue
        my_key = np.array(key)
        neighbor1 = my_key + np.array((1,0))
        neighbor2 = my_key + np.array((0,1))
        neighbor3 = my_key + np.array((0,-1))
        neighbor4 = my_key + np.array((-1,0))
        neighbor5 = my_key + np.array((1,1))
        neighbor6 = my_key + np.array((-1,-1))
        neighbor7 = my_key + np.array((-1,1))
        neighbor8 = my_key + np.array((1,-1))
        neighbors = [neighbor1, neighbor2, neighbor3, neighbor4,
                     neighbor5, neighbor6, neighbor7, neighbor8]
        #logger.info(neighbors)
        values = [entry.get(tuple(neighbor), 0) for neighbor in neighbors]
        #print(values)
        n_n = values.count("#")
        if n_n >= 4 and value == "#":
            new_value = "L"
        elif n_n == 0 and value == "L":
            new_value = "#"
        else:
            new_value = value

        new_entry[key] = new_value

    return new_entry


def neighbor_func(data, key, direction):
    limits = get_limits(data)

    key = np.array(key)
    direction = np.array(direction)
    value = "."
    while (key[0] >= 0 and key[0] <= limits.max_i and
           key[1] >= 0 and key[1] <= limits.max_j):
        key = key + direction
        value = data.get(tuple(key), ".")
        if value != ".":
            break

    return value



def algo2(data):
    new_data = data.copy()
    for key, value in data.items():
        if value == -1:
            continue
        my_key = np.array(key)
        dir1 = (1,0)
        dir2 = (0,1)
        dir3 = (0,-1)
        dir4 = (-1,0)
        dir5 = (1,1)
        dir6 = (-1,-1)
        dir7= (-1,1)
        dir8 = (1,-1)
        directions = [dir1, dir2, dir3, dir4,
                     dir5, dir6, dir7, dir8]
        values = [neighbor_func(data, key, dir) for dir in directions]
        #logger.info(values)

        #print(values)
        n_n = values.count("#")
        if n_n >= 5 and value == "#":
            new_value = "L"
        elif n_n == 0 and value == "L":
            new_value = "#"
        else:
            new_value = value

        new_data[key] = new_value

    return new_data


#def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


#def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 37

def test_task2(testdata):
    assert task2(testdata) == 26

def task(input, subfunc = lambda x: x):
    data = aoc.io.text2subsets(input)
    data = aoc.io.text2dict(data)
    while True:
        next_data = algo1(data)
        viz = aoc.io.dict2text(next_data)
        #print(viz)
        #print("------")
        if np.all(next_data == data):
            break
        data = next_data

    values, counts = np.unique(list(data.values()), return_counts = True)
    logger.info(data.values())
    logger.info(values)
    index = values.tolist().index("#")

    return counts[index]


def task2(input, subfunc = lambda x: x):
    data = aoc.io.text2subsets(input)
    data = aoc.io.text2dict(data)
    while True:
        #viz = aoc.io.dict2text(data)
        #print(viz)
        next_data = algo2(data)
        #print("------")
        if np.all(next_data == data):
            break
        data = next_data

    values, counts = np.unique(list(data.values()), return_counts = True)
    #logger.info(values)
    index = values.tolist().index("#")

    return counts[index]

if __name__ == "__main__":
    data = open("day11_input.txt").read().strip()
    #result1 = task(data)
    #logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
