import numpy as np
import pandas as pd
import io
import re
import sys
from itertools import *

from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return "FBFBBFFRLR"

@fixture()
def testdata2():
    return "BFFFBBFRRR"

@fixture()
def testdata3():
    return "FFFBBBFRRR"

@fixture()
def testdata4():
    return "BBFFBBFRLL"

def test_bsp(testdata, testdata2, testdata3, testdata4):
    assert bsp(testdata) == (44,5,357)
    assert bsp(testdata2) == (70,7,567)
    assert bsp(testdata3) == (14,7,119)
    assert bsp(testdata4) == (102,4,820)


def bsp_helper(input):
    row = range(128)
    column = range(8)
    if len(input[:7]) != 7:
        return 0,0
    assert len(input[:7]) == 7
    for letter in input[:7]:
        if letter == "F":
            row = row[:len(row) // 2]
        elif letter == "B":
            row = row[len(row) // 2:]
    for letter in input[7:]:
        if letter == "L":
            column = column[:len(column) // 2]
        elif letter == "R":
            column = column[len(column) // 2:]
    assert len(row) == 1
    assert len(column) == 1
    return row[0],column[0]

def bsp(input):
    row, column = bsp_helper(input)
    return (row, column, row * 8 + column)

def func(input):
    data = [line.rstrip() for line in input.split("\n")]
    result = [bsp(line) for line in data]
    return result


if __name__ == "__main__":
    #data = [line.rstrip() for line in open("dayx_input.txt").read()]
    data = open("day5_input.txt").read()
    parsed = func(data)
    print(max([x[2] for x in parsed]))
    all_indices = set(list(range(8 * 128)))
    for p in parsed:
        all_indices.remove(p[2])
    print(all_indices)
