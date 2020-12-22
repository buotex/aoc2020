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


def task(input):
    data = aoc.io.text2subsets(input)
    c = Counter(data[0])
    count = 0
    count += c["("]
    count -= c[")"]

    # data = list(map(subfunc, data))
    return count


def task2(input):
    data = aoc.io.text2subsets(input)
    count = 0
    for i, c in enumerate(data[0]):
        if c == "(":
            count += 1
        if c == ")":
            count -= 1
        if count == -1:
            break
    # data = list(map(subfunc, data))
    return i + 1


data = open("puzzles/2015/day1_input.txt").read().strip()
result1 = task(data)
logger.info(result1)
result2 = task2(data)
logger.info(result2)
