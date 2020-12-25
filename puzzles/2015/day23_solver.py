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


def task(input, start_a=0):
    data = aoc.io.text2subsets(input)
    regs = {"a": start_a, "b": 0}
    counter = 0
    while True:
        if counter < 0 or counter >= len(data):
            break
        logger.info(counter)
        logger.info(regs)
        line = data[counter]
        logger.info(line)
        instruction = line[:3]
        arguments = line[3:]
        tokens = re.findall(r"[+-]?\w+", arguments)
        if instruction == "hlf":
            regs[tokens[0]] //= 2
            counter += 1
        if instruction == "tpl":
            regs[tokens[0]] *= 3
            counter += 1
        if instruction == "inc":
            regs[tokens[0]] += 1
            counter += 1
        if instruction == "jmp":
            counter += int(tokens[0])
        if instruction == "jie":
            if regs[tokens[0]] % 2 == 0:
                counter += int(tokens[1])
            else:
                counter += 1
        if instruction == "jio":
            if regs[tokens[0]] == 1:
                counter += int(tokens[1])
            else:
                counter += 1

        # if instruction == "hlf":

    # data = list(map(subfunc, data))
    return regs["b"]


def test_task(testdata):
    assert task(testdata) == 0


def task2(input):
    return task(input, 1)


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day23_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
