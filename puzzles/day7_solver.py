import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools
from collections import defaultdict

from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""




def algo1(entry):
    tokens = entry.split()
    my_dict = {}
    bags = []
    for i in range(4, len(tokens), 4):
        if tokens[i] != "no":
            my_dict[(tokens[i+1], tokens[i+2])] = [(int(tokens[i]), tokens[0], tokens[1])]

    return my_dict


def algo2(entry):
    tokens = entry.split()
    bags = []
    for i in range(4, len(tokens), 4):
        if tokens[i] != "no":
            bags.append((int(tokens[i]), tokens[i+1], tokens[i+2]))
    my_dict = {(tokens[0], tokens[1]): bags}
    return my_dict


def test_subtask1():
    entry = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    assert algo1(entry) == {("bright","white"): [(1, "light", "red")],
                            ("muted", "yellow"): [(2, "light", "red")]}

#def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    visited = task(testdata, algo1)
    logger.info(visited)
    assert len(visited) == 4


def test_task2(testdata):
    visited = task2(testdata, algo2)
    logger.info(visited)
    assert sum(visited) == 32


def task(input, subfunc = lambda x: x):
    data = aoc.io.text2subsets(input)
    target = ("shiny", "gold")
    data = list(map(subfunc, data))
    connectivity = defaultdict(list)
    for entry in data:
        for key, val in entry.items():
            connectivity[key].extend(val)
    # find all predecessors of shiny gold
    logger.info(connectivity)

    result, visited = aoc.graph.search_dict(connectivity, start=("shiny", "gold"))
    logger.info(visited)
    
    visited.remove((("shiny", "gold"), 1))
    return visited


def task2(input, subfunc = lambda x: x):
    data = aoc.io.text2subsets(input)
    start = ("shiny", "gold")
    data = list(map(subfunc, data))
    connectivity = defaultdict(list)
    for entry in data:
        for key, val in entry.items():
            connectivity[key].extend(val)
    # find all predecessors of shiny gold

    result, visited = aoc.graph.search_dict(connectivity, start=("shiny", "gold"), count_func= lambda x, y: x * y)
    
    visited.remove((("shiny", "gold"), 1))
    logger.info(visited)
    counts = [v[1] for v in visited]
    return counts


if __name__ == "__main__":
    data = open("day7_input.txt").read().strip()
    logger.info(len(task(data, algo1)))
    logger.info(sum(task2(data, algo2)))
