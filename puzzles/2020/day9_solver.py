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

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
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
    assert task(testdata, 5) == 127

def test_task2(testdata):
    assert task2(testdata, target_sum=127) == 62

def task(input, preamble = 25):
    data = aoc.io.text2subsets(input)
    subfunc = lambda x: int(x)
    data = list(map(subfunc, data))
    for i, row in enumerate(data[preamble:]):
        # preamble
        preamble_numbers = np.array(data[i:i+preamble])
        possible_sums = preamble_numbers + preamble_numbers[:, np.newaxis]
        #print(preamble_numbers)
        if row not in possible_sums:
            return row

    return -1


def task2(input, target_sum=0):
    data = aoc.io.text2subsets(input)
    subfunc = lambda x: int(x)
    data = list(map(subfunc, data))
    for i, row in enumerate(data):
        # preamble
        cumsums = np.cumsum(data[i:])
        cumsums = cumsums.tolist()
        try:
            found_index = cumsums[1:].index(target_sum)
            print(found_index)
            print(data[i:i+found_index+2])
            return min(data[i:i+found_index+2]) + max(data[i:i+found_index+2])
        except:
            continue


    return -1


if __name__ == "__main__":
    data = open("day9_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data, target_sum=result1)
    print(result2)
