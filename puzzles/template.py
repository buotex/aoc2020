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
    return """
"""

def test_func(testdata):
    assert func(testdata) == 0

def func(input):
    data = [line.rstrip() for line in input.split("\n")]
    return 0


if __name__ == "__main__":
    #data = [line.rstrip() for line in open("dayx_input.txt").read()]
    data = open("dayx_input.txt").read()
    func(testdata)
    func(data)
