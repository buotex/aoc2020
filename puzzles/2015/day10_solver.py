from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations
import re
import sys

import numpy as np
from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")


@fixture()
def testdata():
    return """
    """


def algo1(entry):
    return 0


def algo2(entry):
    return 0


# def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


# def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 0


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def task(input):
    data = list(map(int, input))
    print(data)
    for i in range(50):
        new_data = []
        old_val = data[0]
        counter = 1
        for val in chain(data[1:], [float("Inf")]):
            if val != old_val:
                new_data.append(counter)
                new_data.append(old_val)
                old_val = val
                counter = 1
            else:
                counter += 1
        data = new_data

    # data = list(map(subfunc, data))
    return len(data)


def task2(input):
    # data = list(map(subfunc, data))
    return None


def main():
    data = open("puzzles/2015/day10_input.txt").read().strip()
    data = "1321131112"
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


"main" in __name__ and main()
