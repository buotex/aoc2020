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
    nice = 0
    for line in data:
        vowels = re.findall("[aeiou]", line)
        twice = re.findall(r"(.)\1", line)
        banned = re.findall("(ab)|(cd)|(pq)|(xy)", line)
        if len(vowels) >= 3 and twice and not banned:
            nice += 1

    # data = list(map(subfunc, data))
    return nice


def task2(input):
    data = aoc.io.text2subsets(input)
    nice = 0
    for line in data:
        twice = re.findall(r"(..)\w*\1", line)
        twice2 = re.findall(r"(.)\w\1", line)
        if twice and twice2:
            nice += 1

    # data = list(map(subfunc, data))
    return nice


def main():
    data = open("puzzles/2015/day5_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


main()
