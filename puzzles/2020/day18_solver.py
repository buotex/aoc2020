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
1 + (2 * 3) + (4 * (5 + 6))
"""


def test_expression():
    testdata = "1 + 2 * 3 + 4 * 5 + 6"
    assert eval_expression(testdata.split()) == 71


def test_expression2():
    testdata = "1 + (2 * 3) + (4 * (5 + 6))"
    assert algo1(testdata) == 51


def test_expression3():
    testdata = "2 * 3 + (4 * 5)"
    assert algo2(testdata) == 46


def test_expression4():
    testdata = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    assert algo2(testdata) == 23340


def eval_expression(tokens):

    logger.info(tokens)
    number = 0
    current_operator = "+"
    i = 0
    while i < len(tokens):
        if i == 0:
            current_operator = "+"
        else:
            current_operator = tokens[i - 1]
        logger.info(tokens[i])
        if tokens[i] == "(":
            j = i + 1
            depth = 0
            while j < len(tokens):
                # logger.info(tokens[j])
                if tokens[j] == "(":
                    depth += 1
                if tokens[j] == ")":
                    if depth == 0:
                        next_number = eval_expression(tokens[i + 1 : j])
                        break
                    else:
                        depth -= 1
                j += 1
            i = j + 2
        else:
            next_number = int(tokens[i])
            i += 2

        if current_operator == "+":
            number += next_number
        elif current_operator == "*":
            number *= next_number
    logger.info(number)
    return number


def evaluate_stack(stack):
    number = stack[0]
    i = 1
    while i < len(stack):
        if stack[i] == "+":
            number += stack[i + 1]
            i += 2
        else:
            number *= evaluate_stack(stack[i + 1 :])
            i = len(stack)
    return number


def eval_expression2(tokens):

    logger.info(tokens)
    i = 0
    operator_stack = []
    while i < len(tokens):
        if i == 0:
            operator_stack.append(0)
            operator_stack.append("+")
        else:
            operator_stack.append(tokens[i - 1])
        # logger.info(tokens[i])
        if tokens[i] == "(":
            j = i + 1
            depth = 0
            while j < len(tokens):
                if tokens[j] == "(":
                    depth += 1
                if tokens[j] == ")":
                    if depth == 0:
                        next_number = eval_expression2(tokens[i + 1 : j])
                        break
                    else:
                        depth -= 1
                j += 1
            i = j + 2
        else:
            next_number = int(tokens[i])
            i += 2

        operator_stack.append(next_number)
    # eval operator stack:
    logger.info(operator_stack)

    return evaluate_stack(operator_stack)


def algo1(line):
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    tokens = line.split()

    return eval_expression(tokens)


def algo2(line):
    line = line.replace("(", "( ")
    line = line.replace(")", " )")
    tokens = line.split()
    return eval_expression2(tokens)


# def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


# def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 51


def task(input):
    data = aoc.io.text2subsets(input)
    result = []
    for line in data:
        result.append(algo1(line))
    # data = list(map(subfunc, data))
    return sum(result)


def task2(input):
    data = aoc.io.text2subsets(input)
    result = []
    for line in data:
        result.append(algo2(line))
    # data = list(map(subfunc, data))
    return sum(result)


if __name__ == "__main__":
    data = open("day18_input.txt").read().strip()
    # result1 = task(data)
    # logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
