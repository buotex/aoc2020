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
    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    data = aoc.io.text2subsets(input)
    for i, line in enumerate(data):
        tokens = re.findall("([A-z]+): (\d+)", line)
        match = True
        for token in tokens:
            key = token[0]
            value = int(token[1])
            if target[key] != value:
                match = False
                break
        if match:
            return i + 1

        logger.info(tokens)
    # data = list(map(subfunc, data))
    return None


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    data = aoc.io.text2subsets(input)
    for i, line in enumerate(data):
        tokens = re.findall("([A-z]+): (\d+)", line)
        match = True
        for token in tokens:
            key = token[0]
            value = int(token[1])
            if key in ["cats", "trees"]:
                if value <= target[key]:
                    match = False
                    break
            elif key in ["pomeranians", "goldfish"]:
                if value >= target[key]:
                    match = False
                    break
            else:
                if target[key] != value:
                    match = False
                    break
        if match:
            return i + 1

        logger.info(tokens)
    # data = list(map(subfunc, data))
    return None
    # data = list(map(subfunc, data))
    return None


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day16_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
