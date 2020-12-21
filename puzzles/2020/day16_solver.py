import numpy as np
import re
import sys

from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")


@fixture()
def testdata():
    return """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
    7,1,14

nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12
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
    result, matching, _ = task(testdata)
    assert result == 71


def test_task2(testdata):
    result, matching, _ = task(testdata)
    logger.info(matching)
    assert figure_out_matching(matching)
    # assert task(testdata) == {"class": 12, "row": 11, "seat": 13}


def is_between(x, tag):
    return x >= int(tag[0]) and x <= int(tag[1])


def figure_out_matching(valid_tickets):
    valid_tickets = np.array(valid_tickets)
    logger.info(valid_tickets)
    logger.info(valid_tickets.shape)
    logger.info(valid_tickets[0, 2])
    valid_mapping = valid_tickets.prod(axis=0)
    logger.info(valid_mapping)
    # looping
    matching = []
    for i in range(valid_tickets.shape[1]):
        current_mat = valid_mapping.sum(axis=1)
        logger.info(current_mat == 1)
        if not np.any(current_mat == 1):
            raise Exception("can't continue")
            break
        else:
            index_row = np.where(current_mat == 1)[0][0]
            index_col = int(np.where(valid_mapping[index_row, :] == 1)[0])
            valid_mapping[index_row, :] = 0
            valid_mapping[:, index_col] = 0
            matching.append((index_row, index_col))
            logger.info(index_row)
            logger.info(index_col)
    logger.info(valid_mapping)
    logger.info(matching)

    # return indices
    return matching


def task(input):
    data = aoc.io.text2subsets(input)
    logger.info(data)
    tags = {}
    nearby_tickets = []
    nearby_ticket_section = False
    for line in data[0]:
        groups = re.fullmatch("([^:]+): ([^ ]+) or ([^ ]+)", line)
        if groups:
            low1, high1 = groups[2].split("-")
            low2, high2 = groups[3].split("-")
            tags[groups[1]] = [(low1, high1), (low2, high2)]
            # tags.append([(low1, high1), (low2, high2)])
    for line in data[2]:
        if "nearby tickets:" == line:
            nearby_ticket_section = True
        if nearby_ticket_section:
            tokens = line.split(",")
            nearby_tickets.append(tokens)

    # print(tags)
    nearby_tickets = nearby_tickets[1:]
    error_rate = 0
    matching = []

    for ticket in nearby_tickets:
        ticket_entries = []
        ticket_valid = True
        for entry in ticket:
            entry = int(entry)
            entry_is_valid = []

            for tag, tag_value in tags.items():
                if is_between(entry, tag_value[0]) or is_between(entry, tag_value[1]):
                    entry_is_valid.append(True)
                else:
                    entry_is_valid.append(False)
            if not any(entry_is_valid):
                error_rate += entry
                ticket_valid = False
                break
            else:
                ticket_entries.append(entry_is_valid)
        if ticket_valid:
            matching.append(ticket_entries)

    logger.info(nearby_tickets)
    # data = list(map(subfunc, data))
    return error_rate, matching, tags


def task2(mapping, tags):
    matching = figure_out_matching(mapping)
    tags_list = [(key, value) for (key, value) in tags.items()]
    matching = sorted(matching, key=lambda x: x[1])
    return matching


if __name__ == "__main__":
    data = open("day16_input.txt").read().strip()
    result1, mapping, tags = task(data)
    logger.info(result1)

    matching = task2(mapping, tags)
    logger.info(matching)
    my_ticket = [
        89,
        139,
        79,
        151,
        97,
        67,
        71,
        53,
        59,
        149,
        127,
        131,
        103,
        109,
        137,
        73,
        101,
        83,
        61,
        107,
    ]
    result = [my_ticket[entry[0]] for entry in matching[:6]]
    print(result)
    print(np.prod(result))

    # result2 = task2(data)
    # logger.info(result2)
