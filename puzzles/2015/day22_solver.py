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

import dataclasses


@dataclasses.dataclass
class GameState:
    player_hp: int
    player_mana: int
    boss_hp: int
    boss_damage: int
    player_mana_spent: int = 0
    player_turn: bool = True
    shield: int = 0
    poison: int = 0
    recharge: int = 0

    def __lt__(self, other):
        return self.player_hp < other.player_hp


def play_game(state, hard_mode=True):
    import heapq

    states = [state]
    actions = {"mm": 53, "drain": 73, "shield": 113, "poison": 173, "recharge": 229}
    lengths = {"shield": 6, "poison": 6, "recharge": 5}
    import heapq
    import copy

    while len(states) > 0:
        mana_spent, state = heapq.heappop(states)
        if state.player_turn == 1:
            state.player_hp -= 1

        if state.player_hp <= 0:
            continue
        # logger.info(state)
        player_armor = 0
        if state.shield:
            player_armor = 7
            state.shield -= 1
        if state.poison:
            state.boss_hp -= 3
            state.poison -= 1
        if state.recharge:
            state.player_mana += 101
            state.recharge -= 1
        if state.boss_hp <= 0:
            # win
            return state
        # resolve effects
        if state.player_turn:
            for action, cost in actions.items():
                if cost > state.player_mana:
                    continue
                new_state = copy.copy(state)
                new_state.player_turn = False

                new_state.player_mana_spent += cost
                new_state.player_mana -= cost

                if action == "mm":
                    new_state.boss_hp -= 4
                elif action == "drain":
                    new_state.player_hp += 2
                    new_state.boss_hp -= 2
                else:
                    if getattr(new_state, action) > 0:
                        continue
                    else:
                        setattr(new_state, action, lengths[action])
                heapq.heappush(states, (new_state.player_mana_spent, new_state))
        else:
            # enemy hits
            new_state = copy.copy(state)
            new_state.player_turn = True
            new_state.player_hp -= max(1, new_state.boss_damage - player_armor)
            if new_state.player_hp > 0:
                heapq.heappush(states, (new_state.player_mana_spent, new_state))

    return None


def task(input, hard_mode=False):

    data = aoc.io.text2subsets(input)
    boss_hp = int(re.findall(r"\d+", data[0])[0])
    boss_damage = int(re.findall(r"\d+", data[1])[0])
    state = (0, GameState(50, 500, boss_hp, boss_damage))
    min_mana = play_game(state, hard_mode=hard_mode)

    # heapq.heappush(states, next_state)

    # data = list(map(subfunc, data))
    return min_mana


def test_task():
    state = (0, GameState(10, 250, 13, 8))
    win_state = play_game(state)

    assert win_state.player_mana == 24


def task2(input):
    return task(input, hard_mode=True)


def test_task2(testdata):
    pass
    # assert task2(testdata) == 0


def main():
    data = open("puzzles/2015/day22_input.txt").read().strip()
    result2 = task2(data)
    if result2:
        logger.info(result2)
    else:
        result1 = task(data)
        logger.info(result1)


"main" in __name__ and main()
