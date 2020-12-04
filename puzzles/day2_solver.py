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

def func(input):
    data = pd.read_csv(input, sep=" ", names=["policy", "letter", "password"])
    data.letter = data.letter.str[0]
    logger.info(data.head())
    def test_password(row):
        policy = row.policy
        letter = row.letter
        password = row.password
        limit_lower = int(policy.split("-")[0])
        limit_upper = int(policy.split("-")[1])
        count = len(re.findall(letter, password))
        return count >= limit_lower and count <= limit_upper

    result = data.apply(test_password, axis=1)
    logger.info(result[(result == True)].count())

    def test_password2(row):
        policy = row.policy
        letter = row.letter
        password = row.password
        limit_lower = int(policy.split("-")[0])
        limit_upper = int(policy.split("-")[1])
        return (
            (password[limit_lower - 1] == letter and password[limit_upper - 1] != letter ) 
         or 
            (password[limit_lower - 1] != letter and password[limit_upper - 1] == letter ) 
        )

    result = data.apply(test_password2, axis=1)
    logger.info(result[(result == True)].count())

func(io.StringIO(testdata))
func("./day2_input.txt")
