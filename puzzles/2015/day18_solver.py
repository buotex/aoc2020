from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations, product

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
##.#.#
...##.
#....#
..#...
#.#..#
####.#
    """


def algo1(grid):

    new_grid = {}
    neighborhood = (-1, 0, 1)
    for pos, entry in grid.items():
        count = 0
        for neighbors in product(neighborhood, neighborhood):
            if neighbors == (0, 0):
                continue
            else:
                count += (
                    grid.get((pos[0] + neighbors[0], pos[1] + neighbors[1]), ".") == "#"
                )
        if entry == "#":
            if count == 2 or count == 3:
                new_grid[pos] = "#"
            else:
                new_grid[pos] = "."
        else:
            if count == 3:
                new_grid[pos] = "#"
            else:
                new_grid[pos] = "."

    return new_grid


def algo2(entry):
    return 0


# def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


# def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def task(input, iterations=100):
    grid = aoc.io.text2dict(input)
    import operator

    x_max = max(map(operator.itemgetter(0), grid.keys()))
    y_max = max(map(operator.itemgetter(1), grid.keys()))
    for _ in range(iterations):
        grid[(0, 0)] = "#"
        grid[(0, y_max)] = "#"
        grid[(x_max, 0)] = "#"
        grid[(x_max, y_max)] = "#"
        print(aoc.io.dict2text(grid))
        print()
        grid = algo1(grid)
    # data = list(map(subfunc, data))
    grid[(0, 0)] = "#"
    grid[(0, y_max)] = "#"
    grid[(x_max, 0)] = "#"
    grid[(x_max, y_max)] = "#"
    return Counter(grid.values())["#"]


def test_task(testdata):
    assert task(testdata, 5) == 17


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day18_input.txt").read().strip()
    result1 = task(data)
    logger.info(result1)


"main" in __name__ and main()
