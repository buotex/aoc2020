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
from aoc.pc import (pc, State)
from aoc.utils import (KeyLimits, get_limits, get_neighbors, get_directions)

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


#def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


#def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 0


def task(input):
    data = aoc.io.text2subsets(input)
    #data = list(map(subfunc, data))
    return data


if __name__ == "__main__":
    data = open("dayx_input.txt").read().strip()
    result1 = task(data)
    logger.info(result1)
    #result2 = task2(data)
    #logger.info(result2)