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
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
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


def parse_tiles(line):
    commands = []
    i = 0
    while i < len(line):
        if line[i] == "e":
            commands.append("e")
            i += 1
        elif line[i] == "s":
            commands.append("s" + line[i + 1])
            i += 2
        elif line[i] == "n":
            commands.append("n" + line[i + 1])
            i += 2
        elif line[i] == "w":
            commands.append("w")
            i += 1
    return commands


def parse_commands(command_line):
    position = [0, 0]
    for command in command_line:
        if command == "e":
            position[0] += 1
        if command == "w":
            position[0] -= 1
        if command == "se":
            position[1] += 1
            position[0] += 1
        if command == "sw":
            position[1] += 1
        if command == "ne":
            position[1] -= 1
        if command == "nw":
            position[1] -= 1
            position[0] -= 1

    return tuple(position)


def task(input):
    data = aoc.io.text2subsets(input)
    # create instructions
    command_lines = []
    tiles = defaultdict(bool)
    for line in data:
        command_lines.append(parse_tiles(line))
    for command_line in command_lines:
        print(command_line)
        index = parse_commands(command_line)
        print(index)
        tiles[index] = not tiles[index]

    # data = list(map(subfunc, data))
    return sum(tiles.values()), tiles


def test_task(testdata):
    assert task(testdata) == 0


def flip_tiles(tiles):
    new_tiles = {}
    min_x = min([x[0] for x in tiles.keys()])
    max_x = max([x[0] for x in tiles.keys()])
    min_y = min([x[1] for x in tiles.keys()])
    max_y = max([x[1] for x in tiles.keys()])
    for x in range(min_x - 2, max_x + 2):
        for y in range(min_y - 2, max_y + 2):
            pos = (x, y)
            val = tiles.get(pos, False)
            # neighborhood of tile
            neighbors = [
                tiles.get((pos[0] + 1, pos[1]), False),
                tiles.get((pos[0] - 1, pos[1]), False),
                tiles.get((pos[0] + 1, pos[1] + 1), False),
                tiles.get((pos[0], pos[1] + 1), False),
                tiles.get((pos[0], pos[1] - 1), False),
                tiles.get((pos[0] - 1, pos[1] - 1), False),
            ]
            num_blacks = sum(neighbors)
            if val == True:
                if num_blacks == 0 or num_blacks > 2:
                    new_tiles[pos] = False
                else:
                    new_tiles[pos] = True
            else:
                if num_blacks == 2:
                    new_tiles[pos] = True
                else:
                    new_tiles[pos] = False
    return new_tiles


def task2(input):

    _, tiles = task(input)
    for _ in range(100):
        tiles = flip_tiles(tiles)
    # data = list(map(subfunc, data))
    return sum(tiles.values())


def test_task2(testdata):
    assert task2(testdata) == 0


def main():
    data = open("puzzles/2020/day24_input.txt").read().strip()
    result1 = task(data)
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        logger.info(result1)


"main" in __name__ and main()
