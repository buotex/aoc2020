import numpy as np
import pandas as pd
import io
import re
import sys
from loguru import logger
np.set_printoptions(threshold=np.inf)


import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")
testdata = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def func(data):
    mapping = {".": 0, "#": 1}
    data = aoc.matrix.text2np(data, mapping)
    #logger.info(data) 
    values_31 = func2(data, 3, 1)
    values_11 = func2(data, 1, 1)
    values_51 = func2(data, 5, 1)
    values_71 = func2(data, 7, 1)
    values_12 = func2(data, 1, 2)

    drawing = aoc.matrix.np2text(values_31, {0: ".", 1: "#", 2: "O", 3:"X"})
    logger.info(drawing)
    result = [np.sum(val == 3) for val in [values_11, values_31, values_51, values_71, values_12]]
    logger.info(result)
    logger.info(np.prod(result))
        

def func2(data, right, down):
    rows, columns = data.shape
    logger.info(f"{rows}, {columns}")
    data = data.copy()
    for i, j in zip(range(down, rows, down), range(right, sys.maxsize, right)):
        x = i
        y = j % columns
        data[x, y] += 2
    return data


def draw(data, mapping):
    myfunc = lambda x: mapping[x]
    myfunc_vec = np.vectorize(myfunc)
    result = myfunc_vec(data)
    result = "\n".join(["".join(x) for x in result])
    return result
    


if __name__ == "__main__":

    testdata = testdata.split("\n")
    data = [line.rstrip() for line in open("day3_input.txt")]
    #print(testdata)
    #print(data)
    func(testdata)
    func(data)
