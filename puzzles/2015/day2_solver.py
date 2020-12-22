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
    wrapping_paper = 0
    for line in data:
        l, w, h = re.findall("\d+", line)
        l, w, h = int(l), int(w), int(h)
        wrap = 2 * l * w + 2 * w * h + 2 * h * l
        wrap += min([l * w, w * h, h * l])
        wrapping_paper += wrap

    # data = list(map(subfunc, data))
    return wrapping_paper


def task2(input):
    data = aoc.io.text2subsets(input)
    ribbon_all = 0
    for line in data:
        l, w, h = re.findall("\d+", line)
        l, w, h = int(l), int(w), int(h)
        ribbon_all += l * w * h
        lengths = sorted([l, w, h])
        ribbon_all += 2 * (lengths[0] + lengths[1])
    # data = list(map(subfunc, data))
    return ribbon_all


def main():
    data = open("puzzles/2015/day2_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


main()
