from collections import defaultdict, Counter
import copy
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


def fit(containers, remaining, indices):
    result = []
    if sum(containers) < remaining:
        return result
    if remaining == 0:
        return [indices]
    for i, c in enumerate(containers):
        if not indices or i > indices[-1]:
            if c <= remaining:
                new_indices = indices.copy()
                new_indices.append(i)
                result.extend(fit(containers, remaining - c, new_indices))
    return result


def task(input):
    data = aoc.io.text2subsets(input)
    containers = tuple(map(int, data))
    remaining = 150
    fits = fit(containers, remaining, list())
    return len(fits)


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    data = aoc.io.text2subsets(input)
    containers = tuple(map(int, data))
    remaining = 150
    fits = fit(containers, remaining, list())
    lengths = list(map(len, fits))
    min_containers = min(lengths)
    return Counter(lengths)[min_containers]


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day17_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
