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
R8,R4,R4,R8
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
    lst = [0, (0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]
    for x in input.split(", "):
        lst[0] = (
            (lst[0] + 1 if lst[0] < 3 else 0)
            if x[0] == "R"
            else (lst[0] - 1 if lst[0] > 0 else 3)
        )
        [
            lst.append(
                (lst[-1][0] + lst[1 + lst[0]][0], lst[-1][1] + lst[1 + lst[0]][1])
            )
            for x in range(int(x[1:]))
        ]
    print(
        "part 1:",
        abs(lst[-1][0]) + abs(lst[-1][1]),
        "\n",
        "part 2:",
        abs([x for x in lst if lst[5:].count(x) > 1][0][0])
        + abs([x for x in lst if lst[5:].count(x) > 1][0][1]),
    )
    print(lst)
    # data = list(map(subfunc, data))
    return


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    data = aoc.io.text2subsets(input)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir = 0
    position = [0, 0]
    visited = set()
    for entry in re.findall(r"(L|R)(\w+)", data[0]):
        direction = entry[0]
        if direction == "L":
            dir = (dir - 1) % 4
        elif direction == "R":
            dir = (dir + 1) % 4
        distance = int(entry[1])
        for d in range(distance):
            position[0] += directions[dir][0]
            position[1] += directions[dir][1]
            if tuple(position) in visited:
                break
            visited.add(tuple(position))
        else:
            continue
        break

    return abs(position[0]) + abs(position[1])


def test_task2(testdata):
    assert task2(testdata) == 4


def main():
    data = open("puzzles/2016/day1_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
