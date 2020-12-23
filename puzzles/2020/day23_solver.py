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
389125467
    """


def algo1(entry):
    return 0


def algo2(entry):
    return 0


# def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


def test_task(testdata):
    assert task2(testdata, 9, 10) == [9, 2, 6, 5, 8, 3, 7, 4]


def do_step(cups_dict, current_cup, max_cup=1000001):
    cup1 = cups_dict[current_cup]
    cup2 = cups_dict[cup1]
    cup3 = cups_dict[cup2]
    follow_cup = cups_dict[cup3]
    destination_cup = (current_cup - 1) % max_cup
    while destination_cup not in cups_dict or destination_cup in [cup1, cup2, cup3]:
        destination_cup = (destination_cup - 1) % max_cup
    follow_destination = cups_dict[destination_cup]
    cups_dict[destination_cup] = cup1
    cups_dict[current_cup] = follow_cup
    cups_dict[cup3] = follow_destination
    return cups_dict, follow_cup


def test_task2():
    assert np.prod(task2("389125467", 1000000, 10000000)[:2]) == 149245887792


def task2(input, num_cards, iterations=1000000):

    data = aoc.io.text2subsets(input)
    # data = list(map(subfunc, data))
    cups = list(map(int, data[0]))
    current_cup = cups[0]
    for i in range(len(cups) + 1, num_cards + 1):
        cups.append(i)
    cups_dict = {}
    for cup, next_cup in zip(cups, cups[1:] + [cups[0]]):
        cups_dict[cup] = next_cup

    for _ in range(iterations):
        cups_dict, current_cup = do_step(cups_dict, current_cup, num_cards + 1)
        # logger.info(current_cup)

    result = []
    item = cups_dict[1]
    while item != 1:
        result.append(item)
        item = cups_dict[item]

    return result

    # step1: figure out new index for card1
    # what operations are there?
    # op1
    # step2: reverse operations for neighbors of card1
    # data = list(map(subfunc, data))


def main():
    data = open("puzzles/2020/day23_input.txt").read().strip()
    # result1 = task(data)
    result2 = task2(data, 1000000, 10000000)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


"main" in __name__ and main()
