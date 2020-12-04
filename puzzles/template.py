import numpy as np
import pandas as pd
import io
import re
import sys
from loguru import logger

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

testdata = """
"""


def func(input):
    pass

if __name__ == "__main__":
    testdata = testdata.split("\n")
    data = [line.rstrip() for line in open("dayx_input.txt")]
    func(testdata)
    func(data)
