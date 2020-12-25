from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations, combinations_with_replacement

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
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
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
    data = aoc.io.text2subsets(input)
    ingredients = {}
    for line in data:
        tokens = re.findall(r"-?\w+", line)
        ingredients[tokens[0]] = list(
            map(
                int,
                (
                    tokens[2],
                    tokens[4],
                    tokens[6],
                    tokens[8],
                    tokens[10],
                ),
            )
        )
    print(ingredients)

    points = []

    for comb in combinations_with_replacement(list(ingredients.keys()), 100):
        values = np.array([0, 0, 0, 0, 0])
        for ingredient in comb:
            for i in range(5):
                values[i] += ingredients[ingredient][i]
        values = np.maximum(0, values)
        points.append(np.prod(values[:-1]))

    # data = list(map(subfunc, data))
    return max(points)


def test_task(testdata):
    assert task(testdata) == 62842880


def task2(input):
    data = aoc.io.text2subsets(input)
    ingredients = {}
    for line in data:
        tokens = re.findall(r"-?\w+", line)
        ingredients[tokens[0]] = list(
            map(
                int,
                (
                    tokens[2],
                    tokens[4],
                    tokens[6],
                    tokens[8],
                    tokens[10],
                ),
            )
        )

    points = []

    for comb in combinations_with_replacement(list(ingredients.keys()), 100):
        values = np.array([0, 0, 0, 0, 0])
        for ingredient in comb:
            for i in range(5):
                values[i] += ingredients[ingredient][i]
        values = np.maximum(0, values)
        if values[-1] == 500:
            points.append(np.prod(values[:-1]))

    # data = list(map(subfunc, data))
    return max(points)


def test_task2(testdata):
    assert task2(testdata) == 57600000


def main():
    data = open("puzzles/2015/day15_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
