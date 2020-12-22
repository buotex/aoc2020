from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations
import re
import sys
from operator import or_, and_, invert, lshift, rshift

import numpy as np
from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")


@fixture()
def testdata():
    return """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
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
    assert task(testdata) == 0


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def task(input):
    data = aoc.io.text2subsets(input)
    wires = {}
    operator_dict = {
        "AND": and_,
        "OR": or_,
        "NOT": invert,
        "LSHIFT": lshift,
        "RSHIFT": rshift,
    }
    mappings = data

    def conv_operand(op):
        if re.match(r"[a-z]+", op):
            return wires[op]
        else:
            return int(op)

    while len(mappings) > 0:
        # logger.info(mappings)
        line = mappings.pop(0)
        inp, out = line.split("->")
        out = re.findall(r"\w+", out)[0]
        operands = re.findall(r"[a-z0-9]+", inp)
        operator = re.findall(r"[A-Z]+", inp)

        for op in operands:
            if re.match(r"[a-z]+", op) and op not in wires:
                mappings.append(line)
                break
        else:
            operands = list(map(conv_operand, operands))
            if len(operator) == 0:
                value = operands[0]
                # must be number
            else:
                operator_func = operator_dict[operator[0]]

                if len(operands) == 2:
                    value = operator_func(operands[0], operands[1])
                else:
                    value = operator_func(operands[0])
            wires[out] = value % 65536
            logger.info(wires)

    # data = list(map(subfunc, data))
    return wires


def task2(input):
    input = input.replace("14146", "956")
    return task(input)
    # data = list(map(subfunc, data))


def main():
    data = open("puzzles/2015/day7_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


if __name__ == "__main__":
    main()
