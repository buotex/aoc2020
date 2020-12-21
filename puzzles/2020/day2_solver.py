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
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

def test_password(row):
    policy, letter, password = row.split()
    letter = letter[0]
    limit_lower = int(policy.split("-")[0])
    limit_upper = int(policy.split("-")[1])
    count = len(re.findall(letter, password))
    return count >= limit_lower and count <= limit_upper


def test_password2(row):
    policy, letter, password = row.split()
    letter = letter[0]
    limit_lower = int(policy.split("-")[0])
    limit_upper = int(policy.split("-")[1])
    return (
        (password[limit_lower - 1] == letter and password[limit_upper - 1] != letter ) 
     or 
        (password[limit_lower - 1] != letter and password[limit_upper - 1] == letter ) 
    )


def func(input):
    data = aoc.io.text2subsets(input, test_password)

    return sum(data)

def func2(input):
    data = aoc.io.text2subsets(input, test_password2)

    return sum(data)


if __name__ == "__main__":
    #data = [line.rstrip() for line in open("dayx_input.txt").read()]
    data = open("day2_input.txt").read().strip()
    print(func(data))
    print(func2(data))
