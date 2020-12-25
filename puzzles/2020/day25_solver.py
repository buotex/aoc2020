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
5764801
17807724
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
def loop(num, iterations):
    return pow(num, iterations, 20201227)


def task(input):
    data = aoc.io.text2subsets(input)
    num1 = int(data[0])
    num2 = int(data[1])
    iter1 = 0
    iter2 = 0
    for i in range(10000000):
        if loop(7, i) == num1:

            iter1 = i
            break
    for i in range(10000000):
        if loop(7, i) == num2:
            iter2 = i
            break
    encrypt = loop(num1, iter2)

    # data = list(map(subfunc, data))
    return encrypt


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
    data = open("puzzles/2020/day25_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
