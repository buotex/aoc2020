import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools
from copy import deepcopy, copy

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
Player 1:
9
2
6
3
1

Player 2:
    5
    8
    4
    7
    10
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
    assert task(testdata) == 306


def test_task2(testdata):
    assert task2(testdata) == 291


def task(input):
    data = aoc.io.text2subsets(input)
    deck1 = list(map(int, data[0][1:]))
    deck2 = list(map(int, data[1][1:]))
    print(deck1)
    while len(deck1) and len(deck2) > 0:
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
    # scoring
    logger.info(deck1)
    logger.info(deck2)
    score = 0
    for i, cardval in enumerate(itertools.chain(deck1[::-1], deck2[::-1])):
        score += (i + 1) * cardval

    # data = list(map(subfunc, data))
    return score


def win(player, deck1, deck2, card1, card2):
    if player == 1:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)
    return deck1, deck2


def game(deck1, deck2):
    states_1 = set()
    states_2 = set()

    winner = 0
    while True:
        if len(deck1) == 0:
            winner = 2
            break
        if len(deck2) == 0:
            winner = 1
            break
        hash1 = hash(tuple(deck1))
        hash2 = hash(tuple(deck2))
        if hash1 in states_1 and hash2 in states_2:
            # deck1, deck2 = win(1, deck1, deck2, )
            winner = 1
            break
        else:
            states_1.add(hash1)
            states_2.add(hash2)

        card1, card2 = deck1.pop(0), deck2.pop(0)
        # logger.info(card1)
        # logger.info(card2)
        if card1 <= len(deck1) and card2 <= len(deck2):
            # logger.info("play subgame")
            subgame_winner, _ = game(deepcopy(deck1)[:card1], deepcopy(deck2)[:card2])
            deck1, deck2 = win(subgame_winner, deck1, deck2, card1, card2)
        else:
            # logger.info("playing normal")
            if card1 > card2:
                deck1, deck2 = win(1, deck1, deck2, card1, card2)
            else:
                deck1, deck2 = win(2, deck1, deck2, card1, card2)
        # logger.info(deck1)
        # logger.info(deck2)

    logger.info(deck1)
    logger.info(deck2)
    return winner, (deck1, deck2)[winner - 1]


def task2(input):
    data = aoc.io.text2subsets(input)
    deck1 = list(map(int, data[0][1:]))
    deck2 = list(map(int, data[1][1:]))
    print(deck1)
    # scoring
    logger.info(deck1)
    logger.info(deck2)
    score = 0
    winner, deck = game(deck1, deck2)
    for i, cardval in enumerate(deck[::-1]):
        score += (i + 1) * cardval

    # data = list(map(subfunc, data))
    return score


if __name__ == "__main__":
    data = open("day22_input.txt").read().strip()
    # result1 = task(data)
    # logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
