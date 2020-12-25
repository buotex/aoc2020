from collections import defaultdict, Counter
from functools import cache
import io
from itertools import chain, groupby, permutations, product
import re
import sys

import numpy as np
from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

equipment = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage_one     25     1       0
Damage_two     50     2       0
Damage_three    100     3       0
Defense_one    20     0       1
Defense_two    40     0       2
Defense_three    80     0       3
"""


@fixture()
def testdata():
    return """
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


def equipment_choices():
    data = aoc.io.text2subsets(equipment)
    weapons = {}
    armors = {}
    rings = {}
    for line in data[0][1:]:
        values = re.findall(r"\d+", line)
        name = re.findall(r"\w+", line)
        weapons[name[0]] = (int(values[0]), int(values[1]), int(values[2]))
    for line in data[1][1:]:
        values = re.findall(r"\d+", line)
        name = re.findall(r"\w+", line)
        armors[name[0]] = (int(values[0]), int(values[1]), int(values[2]))
    armors["None"] = (0, 0, 0)
    for line in data[2][1:]:
        values = re.findall(r"\d+", line)
        name = re.findall(r"\w+", line)
        rings[name[0]] = (int(values[0]), int(values[1]), int(values[2]))
    rings["None"] = (0, 0, 0)
    return weapons, armors, rings


def do_fight(equipment):
    own_hp = 100
    enemy_hp = 103
    attack = 0
    defense = 0
    enemy_attack = 9
    enemy_def = 2
    for e in equipment:
        attack += e[1]
        defense += e[2]
    while True:
        enemy_hp -= max(1, attack - enemy_def)
        if enemy_hp <= 0:
            return True
        own_hp -= max(1, enemy_attack - defense)
        if own_hp <= 0:
            return False


def task():
    weapons, armors, rings = equipment_choices()
    best_cost = 0
    for equipment in product(weapons, armors, rings, rings):

        weapon, armor, ring1, ring2 = equipment
        if ring1 == ring2:
            # don't use same ring twice
            continue
        weapon, armor, ring1, ring2 = (
            weapons[weapon],
            armors[armor],
            rings[ring1],
            rings[ring2],
        )
        equipment_cost = sum((weapon[0], armor[0], ring1[0], ring2[0]))
        if equipment_cost < best_cost:
            continue
        fight_result = do_fight((weapon, armor, ring1, ring2))
        if not fight_result:
            print(equipment)
            print(equipment_cost)
            best_cost = equipment_cost

    # data = list(map(subfunc, data))
    return best_cost


def test_task(testdata):
    assert task(testdata) == 0


def task2():
    # data = list(map(subfunc, data))
    return None


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day21_input.txt").read().strip()
    result2 = task2()
    if result2:
        logger.info(result2)
    else:
        result1 = task()
        logger.info(result1)


"main" in __name__ and main()
