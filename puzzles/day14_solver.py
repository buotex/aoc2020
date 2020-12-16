import numpy as np
import pandas as pd
import io
import re
import sys
import copy
import itertools
import functools
import collections

from loguru import logger
from pytest import fixture

import aoc
from aoc.pc import (pc, State)
from aoc.utils import (KeyLimits, get_limits, get_neighbors, get_directions)

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


def algo1(entry):
    return 0

def algo2(entry):
    return 0


def test_groups():
    data = """mask = 1000XX0X0X0X0011XX11110110X101101X01
mem[17353] = 91550
mem[3346] = 113780395
mem[25928] = 15887
mask = 1100X110000111X1X010X101X01110110X01
mem[22673] = 365674634
mem[56387] = 707
mem[59272] = 66101
    """
    data = aoc.io.text2subsets(data)
    groups = make_groups(data)
    assert len(groups) == 2

#def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


#def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0

def apply_mask(mask, memvalue):
    memvalue = "{0:b}".format(memvalue)
    memvalue = memvalue.zfill(36)
    memvalue = [x for x in memvalue]
    #logger.info(memvalue)

    for i, x in enumerate(mask):
        if x != "X":
            memvalue[i] = x
    return int("".join(memvalue), 2)


def apply_mask2(mask, memvalue):
    memvalue = "{0:b}".format(memvalue)
    memvalue = memvalue.zfill(36)
    memvalue = [x for x in memvalue]
    #logger.info(memvalue)
    #logger.info(memvalue)

    for i, x in enumerate(mask):
        if x == "1":
            memvalue[i] = "1"
        elif x == "-1":
            memvalue[i] = "0"
        elif x == "-2":
            memvalue[i] = "1"

    #logger.info(mask)
    #logger.info(memvalue)
    return int("".join(memvalue), 2)


def generate_addresses(mask, memtarget, start_i=0):
    addresses = []
    #logger.error(mask)
    if "X" not in mask:
        addresses.append(apply_mask2(mask, memtarget))
        return addresses
    else:
        for i, x in enumerate(mask):
            if i < start_i:
                continue
            if x == "X":
                mask1 = copy.deepcopy(mask)
                mask2 = copy.deepcopy(mask)
                mask1[i] = '-1'
                mask2[i] = '-2'
                #logger.error(mask1)
                add_1 = generate_addresses(mask1, memtarget, i + 1)
                #logger.error(mask2)
                add_2 = generate_addresses(mask2, memtarget, i + 1)
                addresses.extend(add_1)
                addresses.extend(add_2)
    return addresses


def test_generate_addresses():
    mask = [x for x in "0000000000000000000000000000000000XX"]
    memtarget = 26
    addresses = generate_addresses(mask, memtarget)
    assert len(addresses) == 4




def test_apply():
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    mask = [x for x in mask]
    memvalue = 11
    new_memvalue = apply_mask(mask, memvalue)
    assert new_memvalue == 73

def parse(mask:str, memline):
    mask = [x for x in mask]
    memtarget = memline[0]
    memtarget = re.match(r"mem\[([0-9]+)\]", memtarget)[1]
    memvalue = int(memline[1])
    memtarget = int(memtarget)
    return mask, memtarget, memvalue


def test_parse():
    mask = "1000XX0X0X0X0011XX11110110X101101X01"
    memline = ("mem[17353]", "91550")
    new_mask, memtarget, memvalue = parse(mask, memline)
    assert len(new_mask) == 36
    assert memtarget == 17353
    assert memvalue == 91550


def make_groups(data):
    groups = []
    group = []
    for line in data:
        tokens = [x for x in line.split(" = ")]
        if tokens[0] == "mask":
            groups.append(list())
        groups[-1].append(list(tokens))
    return groups


def test_task(testdata):
    assert task(testdata) == 165


def test_task2():
    testdata = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""
    assert task2(testdata) == 208


def task(input):
    data = aoc.io.text2subsets(input)
    #logger.error(data)
    groups = make_groups(data)
    #logger.error(groups)
    memory = {}
    for group in groups:
        logger.info(groups)
        _, mask = group[0]
        logger.info(mask)
        for memline in group[1:]:
            new_mask, memtarget, memvalue = parse(mask, memline)
            memvalue = apply_mask(mask, memvalue)
            memory[memtarget] = memvalue
            logger.info(memtarget)
            logger.info(memvalue)
            
    #data = list(map(subfunc, data))
    return sum(memory.values())


def task2(input):
    data = aoc.io.text2subsets(input)
    #logger.error(data)
    groups = make_groups(data)
    #logger.error(groups)
    memory = {}
    for group in groups:
        #logger.info(groups)
        _, mask = group[0]
        #logger.info(mask)
        for memline in group[1:]:
            new_mask, memtarget, _ = parse(mask, memline)
            memvalue = int(memline[1])
            addresses = generate_addresses(new_mask, memtarget)
            #logger.info(addresses)
            for address in addresses:
                memory[address] = memvalue
            
    #data = list(map(subfunc, data))
    return sum(memory.values())


if __name__ == "__main__":
    data = open("day14_input.txt").read().strip()
    #result1 = task(data)
    #logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
