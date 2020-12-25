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
    gain = {}
    data = aoc.io.text2subsets(input)
    for line in data:
        tokens = line.split()
        p1 = tokens[0]
        p2 = tokens[-1][:-1]
        change = int(tokens[3])
        if tokens[2] == "lose":
            change = -change
        gain[(p1, p2)] = change
    # data = list(map(subfunc, data))

    overall_happiness = []
    persons = set([x[0] for x in gain.keys()])
    for order in permutations(persons):
        happiness = 0
        print(order)
        for p1, p2 in zip(order, list(order[1:]) + [order[0]]):
            print(p1)
            happiness += gain[(p1, p2)]
            happiness += gain[(p2, p1)]

        overall_happiness.append(happiness)
    return max(overall_happiness)


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    gain = defaultdict(int)
    data = aoc.io.text2subsets(input)
    for line in data:
        tokens = line.split()
        p1 = tokens[0]
        p2 = tokens[-1][:-1]
        change = int(tokens[3])
        if tokens[2] == "lose":
            change = -change
        gain[(p1, p2)] = change
    # data = list(map(subfunc, data))

    overall_happiness = []
    persons = set([x[0] for x in gain.keys()])
    persons.add("me")
    for order in permutations(persons):
        happiness = 0
        for p1, p2 in zip(order, list(order[1:]) + [order[0]]):
            happiness += gain[(p1, p2)]
            happiness += gain[(p2, p1)]

        overall_happiness.append(happiness)
    return max(overall_happiness)


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day13_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
