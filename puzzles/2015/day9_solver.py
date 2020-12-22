from collections import defaultdict, Counter
from copy import deepcopy
from functools import cache
import io
from itertools import chain, groupby, permutations
import re
import sys

import numpy as np
from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")


@fixture()
def testdata():
    return """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
    """


def algo1(entry):
    return 0


def algo2(entry):
    return 0


# def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


# def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 605


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def get_shortest_path(graph, current, visited, weight, target_visited):
    followups = []
    visited.append(current)
    if len(visited) == target_visited:
        logger.info(visited)
        return weight
    if current in graph:
        for neighbor in graph[current]:
            if neighbor[0] not in visited:
                followups.append(
                    get_shortest_path(
                        graph,
                        neighbor[0],
                        deepcopy(visited),
                        weight + neighbor[1],
                        target_visited,
                    )
                )
    if len(followups) == 0:
        return float("Inf")
    return min(followups)


def get_longest_path(graph, current, visited, weight, target_visited):
    followups = []
    visited.append(current)
    if len(visited) == target_visited:
        logger.info(visited)
        return weight
    if current in graph:
        for neighbor in graph[current]:
            if neighbor[0] not in visited:
                followups.append(
                    get_longest_path(
                        graph,
                        neighbor[0],
                        deepcopy(visited),
                        weight + neighbor[1],
                        target_visited,
                    )
                )
    if len(followups) == 0:
        return 0
    return max(followups)


def task(input):
    data = aoc.io.text2subsets(input)
    graph = defaultdict(list)
    cities = set()
    for line in data:
        fr, _, to, _, di = line.split()
        cities.add(fr)
        cities.add(to)
        graph[fr].append((to, int(di)))
        graph[to].append((fr, int(di)))
    logger.info(graph)

    paths = [
        get_shortest_path(graph, node, list(), 0, len(cities)) for node in graph.keys()
    ]
    return min(paths)


def task2(input):
    data = aoc.io.text2subsets(input)
    # data = list(map(subfunc, data))
    graph = defaultdict(list)
    cities = set()
    for line in data:
        fr, _, to, _, di = line.split()
        cities.add(fr)
        cities.add(to)
        graph[fr].append((to, int(di)))
        graph[to].append((fr, int(di)))
    logger.info(graph)

    paths = [
        get_longest_path(graph, node, list(), 0, len(cities)) for node in graph.keys()
    ]
    return max(paths)


def main():
    data = open("puzzles/2015/day9_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


"main" in __name__ and main()
