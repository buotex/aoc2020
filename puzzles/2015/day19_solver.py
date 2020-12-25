from collections import defaultdict, Counter
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
H => HO
H => OH
O => HH

HOH
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


def task(input):
    data = aoc.io.text2subsets(input)
    rules = data[0]
    input_string = data[1][0]
    rules_dict = defaultdict(list)
    molecules = []
    for r in rules:
        tokens = re.findall(r"\w+", r)
        rules_dict[tokens[0]].append(tokens[1])
    for key in rules_dict.keys():
        for match in re.finditer(key, input_string):
            start, end = match.span()
            for repl in rules_dict[key]:
                new_string = input_string[:start] + repl + input_string[end:]
                molecules.append(new_string)
    return len(set(molecules))


def test_task(testdata):
    assert task(testdata) == 4


def get_number_of_replacements(input_string, rules_dict):
    molecules = []
    for key in rules_dict.keys():
        for match in re.finditer(key, input_string):
            start, end = match.span()
            for repl in rules_dict[key]:
                new_string = input_string[:start] + repl + input_string[end:]
                molecules.append(new_string)
    return len(set(molecules))


def task2(input):
    data = aoc.io.text2subsets(input)
    rules = data[0]
    input_string = data[1][0]
    rules_dict = defaultdict(list)
    reversed_rules_dict = {}

    for r in rules:
        tokens = re.findall(r"\w+", r)
        rules_dict[tokens[0]].append(tokens[1])
    for key, mappings in rules_dict.items():
        for entry in mappings:
            if entry in reversed_rules_dict:
                print(entry)
                raise RuntimeError
            reversed_rules_dict[entry] = key
    max_rule_length = max(map(len, reversed_rules_dict.keys()))
    current_string = input_string
    end = len(current_string)
    start = end - 1
    counter = 0
    while True:
        current_token = current_string[start:end]
        if current_token in reversed_rules_dict:
            counter += 1
            current_string = (
                current_string[:start]
                + reversed_rules_dict[current_token]
                + current_string[end:]
            )
            end = len(current_string)
            start = end - 1
        else:
            if end - start > max_rule_length:
                end = end - 1
                start = end - 1
            else:
                start -= 1

        print(current_string)
        if current_string == "e":
            break
    return counter


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day19_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
