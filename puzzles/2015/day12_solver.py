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


def count_values(data):

    if isinstance(data, list):
        return sum([count_values(d) for d in data])
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        else:
            return sum([count_values(d) for d in data.values()])
    else:
        if isinstance(data, int):
            return data
        return 0


def task2(input):
    import json

    data = json.loads(input)

    # data = list(map(subfunc, data))
    return count_values(data)


def main():
    data = open("puzzles/2015/day12_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
