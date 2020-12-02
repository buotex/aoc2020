import numpy as np
import pandas as pd
import io
import re
import sys
from loguru import logger

import aoc2020

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

testdata = """
"""


def func(input):
    data = pd.read_csv(input, sep=" ", names=[])


func(io.StringIO(testdata))
func("./dayx_input.txt")
