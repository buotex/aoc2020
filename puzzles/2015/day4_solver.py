from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations
import re
import sys
import hashlib

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
    for i in range(1000000000):
        hash = str(hashlib.md5((input + str(i)).encode()).hexdigest())
        if re.match("00000", hash):
            return i


def task2(input):
    for i in range(1000000000):
        hash = str(hashlib.md5((input + str(i)).encode()).hexdigest())
        if re.match("000000", hash):
            return i


def main():
    # data = open("puzzles/2015/day4_input.txt").read().strip()
    result1 = task("bgvyzdsv")
    result2 = task2("bgvyzdsv")
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


main()
