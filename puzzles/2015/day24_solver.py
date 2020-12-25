from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations, combinations
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
    if sum(containers) < remaining:
        return False
    if remaining == 0:
        return True
    for i, c in enumerate(containers):
        if not indices or i > indices[-1]:
            if c <= remaining:
                new_indices = indices.copy()
                new_indices.append(i)
                if fit(containers, remaining - c, new_indices):
                    return True
    return False


def task(input, num_groups=3):
    data = aoc.io.text2subsets(input)
    numbers = list(map(int, data))
    target_sum = sum(numbers) // num_groups
    logger.info(target_sum)
    results = []
    for i in range(1, len(numbers)):
        logger.info(i)
        comb = combinations(numbers, i)
        for c in comb:
            if sum(c) != target_sum:
                continue
            else:
                remaining_numbers = set(numbers).difference(set(c))

                fits = fit(
                    sorted(list(remaining_numbers), reverse=True), target_sum, list()
                )
                # check if other 2 groups exist
                if not fits:
                    continue
                quantum = np.prod(c)
                print(c)
                results.append(quantum)
        if results:
            break

    # data = list(map(subfunc, data))
    return min(results)


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    return task(input, 4)


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day24_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
