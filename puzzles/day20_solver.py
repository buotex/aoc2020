import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools
import collections

from loguru import logger
from pytest import fixture

import aoc
from aoc.pc import pc, State
from aoc.utils import KeyLimits, get_limits, get_neighbors, get_directions

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")


@fixture()
def testdata():
    return """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""


seadragon = """
..................#.
#....##....##....###
.#..#..#..#..#..#...
"""


def modify(original_grid):
    do_flip_x = [False, True]
    do_flip_y = [False, True]
    do_rotate = [0, 90]
    grids = []
    for x, y, t in itertools.product(do_flip_x, do_flip_y, do_rotate):
        grid = original_grid.copy()
        if x:
            grid = np.flip(grid, 0)
        if y:
            grid = np.flip(grid, 1)
        if t:
            grid = np.rot90(grid)
        grids.append(grid)
    return grids


def match(grid1, grid2, rel_position):
    if rel_position[0] == 1:
        return np.all(grid1[-1, :] == grid2[0, :])
    if rel_position[0] == -1:
        return np.all(grid1[0, :] == grid2[-1, :])

    if rel_position[1] == 1:
        return np.all(grid1[:, -1] == grid2[:, 0])
    if rel_position[1] == -1:
        return np.all(grid1[:, 0] == grid2[:, -1])
    logger.error("what")
    return True


# def test_subtask1():
#    entry = ""
#    assert algo1(entry) == 0


# def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 20899048083289


def test_task2(testdata):
    assert task2(testdata) == 273


def part1_algo(tiles):
    # test tiles that won't line up
    rel_positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighborhood = collections.defaultdict(lambda: collections.defaultdict(list))
    for tile_nr, tile in tiles.items():
        for i, modified_tile in enumerate(modify(tile)):
            for j, rel_position in enumerate(rel_positions):
                for other_tile_nr, other_tile in tiles.items():
                    if other_tile_nr == tile_nr:
                        continue
                    for k, modified_other_tile in enumerate(modify(other_tile)):
                        if match(modified_tile, modified_other_tile, rel_position):
                            neighborhood[(int(tile_nr), i)][rel_position].append(
                                (int(other_tile_nr), k)
                            )
        print(tile_nr)
    return neighborhood


def task(input):
    data = aoc.io.text2subsets(input)
    tiles = {}
    for block in data:
        tile_nr = block[0].split()[1][:-1]
        tile_data = aoc.io.text2grid(block[1:])
        tiles[tile_nr] = tile_data
    neighborhood = part1_algo(tiles)

    possible_positions = {}
    for key, item in neighborhood.items():
        possible_positions[key] = len(list(item.keys()))
    corner_tiles = [key[0] for (key, item) in possible_positions.items() if item == 2]
    return np.prod(np.unique(corner_tiles))
    # data = list(map(subfunc, data))
    # return data


def task2(input):
    data = aoc.io.text2subsets(input)
    tiles = {}
    for block in data:
        tile_nr = int(block[0].split()[1][:-1])
        tile_data = aoc.io.text2grid(block[1:])
        tiles[tile_nr] = tile_data
    neighborhood = part1_algo(tiles)

    possible_positions = {}
    left_corner_tile = [
        key
        for key, item in neighborhood.items()
        if sorted(list(item.keys()), key=lambda x: x[0]) == [(0, 1), (1, 0)]
    ]
    grid_size = int(np.sqrt(len(neighborhood.keys()) // 8))
    logger.info(grid_size)
    current_position = (0, 0)
    stack = []
    all_tile_nrs = set(np.unique([key[0] for key in neighborhood.keys()]))
    logger.info(all_tile_nrs)

    direction = (1, 0)
    for current_tile in left_corner_tile:
        stack.append((current_tile, current_position, all_tile_nrs, direction))
    current_grid = {}

    while len(stack) > 0:
        current_tile, current_position, available_tiles, direction = stack.pop()
        # test if matching to previous ones?
        # insert
        current_grid[current_position] = current_tile
        next_position = (
            current_position[0] + direction[0],
            current_position[1] + direction[1],
        )
        next_direction = direction
        if next_position[0] < 0 or next_position[0] >= grid_size:
            next_position = (
                current_position[0],
                current_position[1] + 1,
            )
            # flip direction
            next_direction = (-direction[0], 0)
            direction = (0, 1)
        if next_position[1] >= grid_size:
            break
        logger.info(next_position)

        next_available_tiles = available_tiles.copy()
        next_available_tiles.remove(current_tile[0])

        logger.info(direction)
        for neighbor in neighborhood[current_tile][direction]:
            if neighbor[0] not in next_available_tiles:
                continue
            above = (next_position[0], next_position[1] - 1)
            if above[1] != -1:
                if neighbor not in neighborhood[current_grid[above]][(0, 1)]:
                    continue

            stack.append(
                (neighbor, next_position, next_available_tiles, next_direction)
            )

    logger.info(current_grid)
    picture_dict = {
        key: modify(tiles[item[0]])[item[1]] for key, item in current_grid.items()
    }
    logger.info(picture_dict)
    picture = np.vstack([picture_dict[j, 0][1:-1, 1:-1] for j in range(grid_size)])
    for i in range(1, grid_size):
        new_column = np.vstack(
            [picture_dict[j, i][1:-1, 1:-1] for j in range(grid_size)]
        )
        picture = np.hstack((picture, new_column))

    # logger.info(aoc.io.grid2text(picture))
    my_seadragon = aoc.io.text2grid(aoc.io.text2subsets(seadragon))
    roughness = 0
    for modified in modify(picture):
        seadragon_count = 0
        for i in range(picture.shape[0] - my_seadragon.shape[0]):
            for j in range(picture.shape[1] - my_seadragon.shape[1]):
                comp_picture = modified[
                    i : i + my_seadragon.shape[0], j : j + my_seadragon.shape[1]
                ]
                if np.all(comp_picture[my_seadragon == "#"] == "#"):
                    comp_picture[my_seadragon == "#"] = "O"
                    seadragon_count += 1
                    modified[
                        i : i + my_seadragon.shape[0], j : j + my_seadragon.shape[1]
                    ] = comp_picture
                # find_seadragon
        if seadragon_count > 0:
            print(aoc.io.grid2text(modified))
            roughness = np.sum(modified == "#")
            logger.info(roughness)
            continue

    return roughness

    # for key, item in neighborhood.items():
    #    possible_positions[key] = len(list(item.keys()))
    # corner_tiles = [key for (key, item) in possible_positions.items() if item == 2]
    # side_tiles = [key for (key, item) in possible_positions.items() if item == 3]
    # inner_tiles = [key for (key, item) in possible_positions.items() if item == 4]

    # arrange tiles


if __name__ == "__main__":
    data = open("day20_input.txt").read().strip()
    # result1 = task(data)
    # logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
