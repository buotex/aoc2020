import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools

from loguru import logger
from pytest import fixture

import aoc
from aoc.pc import (pc, State)
from aoc.utils import (KeyLimits, get_limits, get_neighbors, get_directions)

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """
939
7,13,x,x,59,x,31,19
"""


def algo1(entry):
    return 0

def algo2(entry):
    return 0


#def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


#def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):

    assert task(testdata) == 295

def test_task2(testdata):
    #task2(testdata)
    assert task2(testdata) == 1068781


def test_crt():
    assert crt([3,4,5], [2,3,2]) == 47

def test_crt2():
    assert crt([3,5,7], [2,3,2]) == (23)

def test_task2_1():
    testdata_1 = """
0
17,x,13,19
"""
    assert task2(testdata_1) == 3417


def task(input):
    data = aoc.io.text2subsets(input)
    my_timestamp = int(data[0])
    bus_ids = data[1].split(",")
    bus_ids = [int(id) for id in bus_ids if id != 'x']
    waiting_times = []
    for bus_id in bus_ids:
        bus_time = my_timestamp - my_timestamp % bus_id
        bus_time += bus_id
        waiting_times.append(bus_time)

    index = waiting_times.index(min(waiting_times))

    #data = list(map(subfunc, data))
    return bus_ids[index] * (waiting_times[index] - my_timestamp)


def extended_euclid(x, y):
    if y == 0:
        return (x, 1, 0)
    (d_, s_, t_) = extended_euclid(y, x % y)
    (d, s, t) = (d_, t_, s_ - (x // y) * t_)
    return (d, s, t)


def test_euclid():
    assert extended_euclid(3, 20) == (1, 7, -1)


def crt(values, target_rem):
    all_multiplied = functools.reduce(lambda x, y: x * y, values)
    logger.error(all_multiplied)
    logger.error(values)
    logger.error(target_rem)
    remainders = []
    for val, rem in zip(values, target_rem):
        other_val = all_multiplied // val
        remainder, mult1, mult2 = extended_euclid(val, other_val)
        #logger.error(remainder)
        #logger.error(mult1)
        #logger.error(mult2)
        remainders.append(rem * other_val * mult2)

    logger.error(remainders)
    return (sum(remainders) % all_multiplied)


def task2(input):
    data = aoc.io.text2subsets(input)
    bus_ids = data[1].split(",")

    def inter(x):
        if x != "x":
            return int(x)
        else:
            return x

    bus_ids = [inter(id) for id in bus_ids]
    values = []
    target_rem = []
    for i, bus_id in enumerate(bus_ids):
        if bus_id == "x":
            continue
        values.append(bus_id)
        target_rem.append(-i)

    return crt(values, target_rem)

    #print(waiting_times)
    #index = waiting_times.index(min(waiting_times))

    ##data = list(map(subfunc, data))
    #return bus_ids[index] * (waiting_times[index] - my_timestamp)

if __name__ == "__main__":
    data = open("day13_input.txt").read().strip()
    #result1 = task(data)
    #logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
