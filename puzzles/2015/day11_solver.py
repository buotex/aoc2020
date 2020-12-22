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


def conv(p):
    return "".join(map(chr, p))


def test_pass():
    password = list(map(ord, "aaaaa"))
    assert conv(get_next_password(password)) == "aaaab"
    password = list(map(ord, "bbbbb"))
    assert conv(get_next_password(password)) == "bbbbc"
    password = list(map(ord, "aaaaz"))
    assert conv(get_next_password(password)) == "aaaba"


def test_task(testdata):
    assert task(testdata) == 0


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def get_next_password(password):
    new_password = []
    up = 1
    for p in password[::-1]:
        if up:
            p_new = p + 1
            up = 0
        else:
            p_new = p
        if p_new > ord("z"):
            p_new = ord("a")
            up = 1
        new_password.append(p_new)
    return new_password[::-1]


def task(input):
    data = aoc.io.text2subsets(input)
    password = list(map(ord, data[0]))

    while conv(password) != "zzzzzzzz":
        logger.info(conv(password))
        password = get_next_password(password)
        good_pass = True
        for p in password:
            if chr(p) in ["i", "o", "l"]:
                good_pass = False
                break
        diff = [x - y for x, y in zip(password[1:], password[:-1])]
        for (x, y, z) in zip(diff, diff[1:], diff[2:]):
            if x == 1 and y == 1 and z == 1:
                good_pass &= True
                break
        else:
            good_pass = False
        for i, (a, b) in enumerate(zip(diff, diff[2:])):
            if a == b == 0:
                if password[i] != password[i + 2]:
                    good_pass &= True
                    break
        else:
            good_pass = False
        if good_pass:
            break

    # data = list(map(subfunc, data))
    return "".join(map(chr, password))


def task2(input):
    data = aoc.io.text2subsets(input)
    # data = list(map(subfunc, data))
    return None


def main():
    data = open("puzzles/2015/day11_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


"main" in __name__ and main()
