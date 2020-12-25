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
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
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


def task(input, limit=2503):
    data = aoc.io.text2subsets(input)
    reindeers = []
    for line in data:
        tokens = re.findall(r"\d+", line)
        reindeers.append(list(map(int, tokens)))
    distance = []
    for r in reindeers:
        steps = limit // (r[1] + r[2])
        print(steps)
        remainder = min(limit - steps * (r[1] + r[2]), r[1])
        seconds = remainder + steps * r[1]
        print(seconds)
        distance.append(seconds * r[0])
    # data = list(map(subfunc, data))
    return max(distance)


def test_task(testdata):
    assert task(testdata, 1000) == 1120


def task2(input, limit=2503):
    data = aoc.io.text2subsets(input)
    reindeers = []
    for line in data:
        tokens = re.findall(r"\d+", line)
        reindeers.append(list(map(int, tokens)))
    scores = np.array([0 for _ in reindeers])
    distances = np.array([0 for _ in reindeers])
    for second in range(0, limit):
        for i, r in enumerate(reindeers):
            steps = second // (r[1] + r[2])
            print(steps)
            remainder = second - steps * (r[1] + r[2])
            if remainder < r[1]:
                distances[i] += r[0]
        scores[distances == max(distances)] += 1

    # data = list(map(subfunc, data))
    print(distances)
    print(scores)
    return max(scores)


def test_task2(testdata):
    assert task2(testdata, 1000) == 689
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day14_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
