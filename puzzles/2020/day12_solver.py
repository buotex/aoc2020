import re
import sys

from loguru import logger
from pytest import fixture

import aoc
import os

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """
F10
N3
F7
R90
F11
"""


def move_forward(ship_x, ship_y, waypoint_x, waypoint_y, count):
    ship_x += waypoint_x * count
    ship_y += waypoint_y * count
    return ship_x, ship_y


def rotate_waypoint(waypoint_x, waypoint_y, turn, degrees):
    for _ in range(degrees // 90):
        if turn == "right":
            waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        else:
            waypoint_x, waypoint_y = waypoint_y, -waypoint_x

    return waypoint_x, waypoint_y



def move_dir(moved_x, moved_y, direction, count):
    if direction == "N":
        moved_y -= count
    elif direction == "S":
        moved_y += count
    elif direction == "E":
        moved_x += count
    elif direction == "W":
        moved_x -= count

    return moved_x, moved_y


def test_subtask2():
    new_rot = rotate_waypoint(1,0, "right", 90)
    print(new_rot)
    assert new_rot[0] == 0
    assert new_rot[1] == 1


def test_task(testdata):
    assert task(testdata) == 25

def test_task2(testdata):
    assert task(testdata, waypoint=(10,-1), mode="other") == 286



def task(input, waypoint = (1,0), mode="ship"):
    data = aoc.io.text2subsets(input)

    def subfunc(line):
        tokens = re.fullmatch(r"([A-Z])([0-9]*)", line)
        return [tokens.group(1), int(tokens.group(2))]
    data = list(map(subfunc, data))
    waypoint_x, waypoint_y = waypoint
    ship_x = 0
    ship_y = 0
    directions = ["N", "W", "E", "S"]

    for order, count in data:
        if order in directions:
            if mode == "ship":
                ship_x, ship_y = move_dir(ship_x, ship_y, order, count)
            else:
                waypoint_x, waypoint_y = move_dir(waypoint_x, waypoint_y, order, count)
        elif order == "L":
            waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, "left", count)
        elif order == "R":
            waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, "right", count)
        elif order == "F":
            ship_x, ship_y= move_forward(ship_x, ship_y, waypoint_x, waypoint_y, count)
        #logger.info(f"{ship_x}, {ship_y}")
        #logger.info(f"{waypoint_x}, {waypoint_y}")
    return abs(ship_x) + abs(ship_y)



if __name__ == "__main__":
    data = open("day12_input.txt").read().strip()
    result1 = task(data)
    logger.info(result1)
    result2 = task(data, waypoint=(10,-1), mode="other")
    logger.info(result2)
