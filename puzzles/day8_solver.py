import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools
from dataclasses import dataclass
import copy

from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

@dataclass
class State:
    pointer = 0
    acc = 0

def algo1(data, state):
    tokens = data[state.pointer]
    instruction, argument = tokens.split()
    argument = int(argument)
    if instruction == "jmp":
        state.pointer += argument
    else:
        state.pointer += 1
    if instruction == "acc":
        state.acc += argument

    return state


def test_task(testdata):
    state, _ = task(testdata)
    assert state.acc == 5

def test_task2(testdata):
    state, _ = task2(testdata)
    assert state.acc == 8

def pc(data, state):
    used_pointers = set()
    state = State()
    graceful_terminate = True
    while True:
        if state.pointer >= len(data):
            graceful_terminate = True
            break
        if state.pointer in used_pointers:
            graceful_terminate = False
            break
        used_pointers.add(state.pointer)
        state = algo1(data, state)
    #data = list(map(subfunc, data))
    return state, graceful_terminate


def task(input):
    data = aoc.io.text2subsets(input)
    state = State()
    state, graceful_terminate = pc(data, state)
    return state, graceful_terminate


def task2(input):
    data = aoc.io.text2subsets(input)
    for i, line in enumerate(data):
        data_copy = copy.deepcopy(data)
        data_copy[i] = line.replace("nop", "jmp")
        state = State()
        state, graceful_terminate = pc(data_copy, state)
        if graceful_terminate == True:
            return state, graceful_terminate

    for i, line in enumerate(data):
        data_copy = copy.deepcopy(data)
        data_copy[i] = line.replace("jmp", "nop")
        state = State()
        state, graceful_terminate = pc(data_copy, state)
        if graceful_terminate == True:
            return state, graceful_terminate
    return state, graceful_terminate



if __name__ == "__main__":
    data = open("day8_input.txt").read().strip()
    state, graceful_terminate = task(data)
    logger.info(state.acc)
    #logger.info(state.acc)
    state, graceful_terminate = task2(data)
    logger.info(state.acc)
