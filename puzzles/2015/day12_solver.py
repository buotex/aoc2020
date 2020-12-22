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
[-1,{"a":1}]
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
    # assert task(testdata) == 0
    assert task("""{"a":{"b":4},"c":-1}""") == 3


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def task(input):
    val = 0
    print(input)
    vals = list(map(int, re.findall(r"-?\d+\.?\d*", input)))
    return sum(list(vals))
    # data = aoc.io.text2subsets(input)

    # data = list(map(subfunc, data))


def task2(input):
    data = aoc.io.text2subsets(input)
    # data = list(map(subfunc, data))
    return None


def main():
    data = open("puzzles/2015/day12_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


"main" in __name__ and main()
