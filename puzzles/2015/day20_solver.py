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


def get_divisors(num):
    return [x for x in range(1, num + 1) if num % x == 0]


def task(input):
    data = aoc.io.text2subsets(input)
    target_sum = int(data[0])

    houses = np.zeros(10000000)
    for i in range(1, 1000000):
        houses[i : 50 * i + 1 : i] += 11 * i
    logger.info(target_sum)
    result = np.where(houses >= target_sum)
    return result


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
    data = open("puzzles/2015/day20_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
