import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools
from collections import defaultdict

from loguru import logger
from pytest import fixture

import aoc
from aoc.pc import (pc, State)
from aoc.utils import (KeyLimits, get_limits, get_neighbors, get_directions)

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return [0,3,6]


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
    assert task(testdata, 10) == 0
    assert task(testdata, 9) == 4

def test_task(testdata):
    assert task(testdata, 30000000) == 175594


def task(input, limit = 2020):
    visited = {}
    for i, x in enumerate(input):
        visited[x] = i+1

    i = len(input)
    last_number = input[-1]
    while i < limit:
        i += 1
        #logger.info(visited)
        if last_number not in visited:
            saying = 0
        else:
            saying = i - 1 - visited[last_number]
        visited[last_number] = i - 1
        #visited[saying] = i
        last_number = saying
        #logger.info(saying)
    return last_number 


if __name__ == "__main__":
    #data = open("day15_input.txt").read().strip()
    data = [6,13,1,15,2,0]
    result1 = task(data, 30000000)
    logger.info(result1)
    #result2 = task2(data)
    #logger.info(result2)
