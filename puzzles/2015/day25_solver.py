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


def task(input):
    target_row = 3010
    target_column = 3019
    row = 1
    column = 1
    val = 20151125
    mult = 252533
    mod = 33554393
    while row != target_row or column != target_column:
        if row == 1:
            row = column + 1
            column = 1
        else:
            row -= 1
            column += 1
        val = val * mult % mod

    # index of this is...

    # data = list(map(subfunc, data))
    return val


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    data = aoc.io.text2subsets(input)
    # data = list(map(subfunc, data))
    return None


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day25_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
