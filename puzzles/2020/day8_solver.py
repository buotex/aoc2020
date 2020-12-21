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
from aoc.pc import *

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


def test_task(testdata):
    state, _ = task(testdata)
    assert state.acc == 5

def test_task2(testdata):
    state, _ = task2(testdata)
    assert state.acc == 8


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
    raise RuntimeError("PC doesn't terminate at all")



if __name__ == "__main__":
    data = open("day8_input.txt").read().strip()
    state, graceful_terminate = task(data)
    logger.info(state.acc)
    #logger.info(state.acc)
    state, graceful_terminate = task2(data)
    logger.info(state.acc)
