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
    houses = defaultdict(int)
    pos = (0, 0)
    houses[pos] += 1
    for l in data[0]:
        if l == ">":
            pos = (pos[0] + 1, pos[1])
        if l == "<":
            pos = (pos[0] - 1, pos[1])
        if l == "^":
            pos = (pos[0], pos[1] + 1)
        if l == "v":
            pos = (pos[0], pos[1] - 1)
        houses[pos] += 1

    # data = list(map(subfunc, data))
    return len(list(houses.keys()))


def task2(input):
    data = aoc.io.text2subsets(input)
    data = aoc.io.text2subsets(input)
    houses = defaultdict(int)
    both_pos = [(0, 0), (0, 0)]
    houses[both_pos[0]] += 1
    for i, l in enumerate(data[0]):
        index = i % 2
        pos = both_pos[index]
        if l == ">":
            pos = (pos[0] + 1, pos[1])
        if l == "<":
            pos = (pos[0] - 1, pos[1])
        if l == "^":
            pos = (pos[0], pos[1] + 1)
        if l == "v":
            pos = (pos[0], pos[1] - 1)
        houses[pos] += 1
        both_pos[index] = pos

    # data = list(map(subfunc, data))
    return len(list(houses.keys()))
    # data = list(map(subfunc, data))
    return None


def main():
    data = open("puzzles/2015/day3_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


main()
