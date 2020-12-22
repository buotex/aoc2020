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
    data = aoc.io.text2subsets(input)
    area = np.zeros((1000, 1000), dtype=bool)
    for line in data:
        commands = re.findall(r"\w+", line)
        limits = list(map(int, re.findall(r"\d+", line)))
        if commands[0] == "turn":
            if commands[1] == "off":
                area[limits[0] : limits[2] + 1, limits[1] : limits[3] + 1] = 0
            else:
                area[limits[0] : limits[2] + 1, limits[1] : limits[3] + 1] = 1
        else:
            area[limits[0] : limits[2] + 1, limits[1] : limits[3] + 1] = ~area[
                limits[0] : limits[2] + 1, limits[1] : limits[3] + 1
            ]

    # data = list(map(subfunc, data))
    return np.sum(area)


def task2(input):
    data = aoc.io.text2subsets(input)
    area = np.zeros((1000, 1000), dtype=int)
    for line in data:
        commands = re.findall(r"\w+", line)
        limits = list(map(int, re.findall(r"\d+", line)))
        if commands[0] == "turn":
            if commands[1] == "off":
                area[limits[0] : limits[2] + 1, limits[1] : limits[3] + 1] -= 1
                area = np.maximum(0, area)
            else:
                area[limits[0] : limits[2] + 1, limits[1] : limits[3] + 1] += 1
        else:
            area[limits[0] : limits[2] + 1, limits[1] : limits[3] + 1] += 2

    # data = list(map(subfunc, data))
    return np.sum(area)


def main():
    data = open("puzzles/2015/day6_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


main()
