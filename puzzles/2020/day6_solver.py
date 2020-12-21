import numpy as np
import pandas as pd
import io
import re
import sys
import functools
import string
from itertools import *

from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """abc

a
b
c

ab
ac

a
a
a
a

b"""

def testdata2():
    entry = """vus
uvs
vwups"""


def any(entry):
    sets = map(set, entry)
    any = functools.reduce(lambda x,y: x.union(y), sets)

    return len(any)


def all(entry):
    sets = map(set, entry)
    intersection = functools.reduce(lambda x,y: x.intersection(y), sets)

    return len(intersection)


def test_entry():
    entry = """vus
uvs
vwups"""
    assert all(entry.split("\n")) == 3


def test_func(testdata):
    assert aoc.io.text2subsets(testdata, any) == [3,3,3,1,1]


def test_func2(testdata):
    assert aoc.io.text2subsets(testdata, all) == [3,0,1,1,1]


if __name__ == "__main__":
    #data = [line.rstrip() for line in open("dayx_input.txt").read()]
    data = open("day6_input.txt").read().strip()
    #print(func(data))
    print(sum(aoc.io.text2subsets(data, all)))
