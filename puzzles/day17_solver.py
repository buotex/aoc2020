import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools

from loguru import logger
from pytest import fixture

import aoc
from aoc.pc import pc, State
from aoc.utils import KeyLimits, get_limits, get_neighbors, get_directions

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")


@fixture()
def testdata():
    return """
.#.
..#
###
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

    assert task(testdata) == 848


def get_new_val(data, key, value):
    active_count = 0
    for x_diff in [-1, 0, 1]:
        for y_diff in [-1, 0, 1]:
            for z_diff in [-1, 0, 1]:
                for a_diff in [-1, 0, 1]:
                    if x_diff == 0 and y_diff == 0 and z_diff == 0 and a_diff == 0:
                        continue
                    if (
                        data.get(
                            (
                                key[0] + x_diff,
                                key[1] + y_diff,
                                key[2] + z_diff,
                                key[3] + a_diff,
                            ),
                            ".",
                        )
                        == "#"
                    ):
                        active_count += 1
    # logger.info(active_count)
    if value == "#":
        if active_count == 2 or active_count == 3:
            return "#"
        else:
            return "."
    else:
        if active_count == 3:
            return "#"
        else:
            return "."


def do_iter(data):
    new_data = {}
    max_x = max(data.keys(), key=lambda x: x[0])[0]
    min_x = min(data.keys(), key=lambda x: x[0])[0]
    max_y = max(data.keys(), key=lambda x: x[1])[1]
    min_y = min(data.keys(), key=lambda x: x[1])[1]
    max_z = max(data.keys(), key=lambda x: x[2])[2]
    min_z = min(data.keys(), key=lambda x: x[2])[2]
    max_a = max(data.keys(), key=lambda x: x[3])[3]
    min_a = min(data.keys(), key=lambda x: x[3])[3]
    for x in range(min_x - 2, max_x + 3):
        for y in range(min_y - 2, max_y + 3):
            for z in range(min_z - 2, max_z + 3):
                for a in range(min_a - 2, max_a + 3):
                    key = (x, y, z, a)
                    new_data[key] = get_new_val(data, key, data.get(key, "."))

    return new_data


def task(input):
    new_data = {}
    data = aoc.io.text2dict(input)
    for key, value in data.items():
        new_key = (int(key[0]), int(key[1]), 0, 0)
        new_data[new_key] = value
    data = new_data
    for i in range(6):
        data = do_iter(data)
    logger.info(data)
    target_sum = len([x for x in data.values() if x == "#"])
    return target_sum


if __name__ == "__main__":
    data = open("day17_input.txt").read().strip()
    result1 = task(data)
    logger.info(result1)
    # result2 = task2(data)
    # logger.info(result2)
