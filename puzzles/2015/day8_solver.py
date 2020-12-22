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
    import ast

    count = 0
    data = aoc.io.text2subsets(input)
    for line in data:
        count += len(line) - len(ast.literal_eval(line))
    # data = list(map(subfunc, data))
    return count


def task2(input):
    data = aoc.io.text2subsets(input)
    count = 0
    for line in data:
        count += len(re.findall('"', line)) + len(re.findall(r"\\", line)) + 2
    # data = list(map(subfunc, data))
    return count


def main():
    data = open("puzzles/2015/day8_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


if __name__ == "__main__":
    main()
