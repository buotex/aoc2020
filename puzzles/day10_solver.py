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
16
10
15
5
1
11
7
19
6
12
4
"""

@fixture()
def testdata2():
    return """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

def algo1(data):
    differences = np.diff(np.array(data), prepend=0, append=(data[-1]+3))

    return differences

def algo2(data, _start_index, _current_diff):

    data = tuple([x for x in data])
    @functools.cache
    def cached_algo(start_index, current_diff):
        if start_index == len(data) - 1:
            return 1
        else: 
            if current_diff + data[start_index + 1] <= 3:
                return cached_algo(start_index + 1, current_diff + data[start_index]) + cached_algo(start_index + 1, current_diff)
            else:
                return cached_algo(start_index + 1, data[start_index+1])
    return cached_algo(_start_index, _current_diff)


#def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


#def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    print(task(testdata))
    assert task(testdata) == 35

def test_task(testdata):
    print(task2(testdata))
    assert task2(testdata) == 8

def test_task(testdata2):
    print(task2(testdata2))
    assert task2(testdata2) == 19208

def task(input):
    data = aoc.io.text2subsets(input)
    data = list(map(int, data))
    data = sorted(data)
    differences = algo1(data)
    unique, counts = np.unique(differences, return_counts = True)
    unique = unique.tolist()
    print(unique, counts)
    return counts[unique.index(1)] * counts[unique.index(3)]

def task2(input):
    data = aoc.io.text2subsets(input)
    data = list(map(int, data))
    data = sorted(data)
    differences = algo1(data)
    logger.info(differences)
    result = algo2(differences, 0, _current_diff=differences[0])
    print(result)

    return result
            

if __name__ == "__main__":
    data = open("day10_input.txt").read().strip()
    #logger.info(task(data))
    logger.info(task2(data))
