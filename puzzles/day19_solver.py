import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools

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
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


def algo1(data):
    parser_dict = {}
    for line in data:
        tokens = line.split(":")
        parser_dict[tokens[0]] = " ".join(tokens[1].strip().split())
    logger.info(parser_dict)

    def replacer(match_obj):
        if match_obj.group(0) in ["8", "11"]:
            return match_obj.group(0)
        return f"({parser_dict[match_obj.group(0)]})"

    revolutions = 0
    while True:
        old_dict = parser_dict.copy()
        if not re.findall("[0-9]", parser_dict["0"]):
            break
        for key, value in parser_dict.items():
            new_value = re.sub("([0-9]+)", replacer, value)
            parser_dict[key] = new_value
        logger.info(revolutions)
        revolutions += 1
        logger.info(parser_dict["0"])
        if old_dict == parser_dict:
            break

    for key, value in parser_dict.items():
        new_value = value.replace(" ", "")
        new_value = new_value.replace('"', "")
        parser_dict[key] = new_value
    return parser_dict


def test_subtask1():
    entry = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
    """
    result = algo1(aoc.io.text2subsets(entry))
    logger.info(result)


def test_subtask2():
    entry = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
    """
    result = task((entry))
    logger.info(result)
    # assert result == 3
    entry = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31 | 42 11 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8 
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
    """
    result = task2((entry))
    logger.info(result)
    assert result == 12


# def test_subtask2():
#    entry = ""
#    assert algo2(entry) == 0


def test_task(testdata):
    assert task(testdata) == 2


def task(input):
    data = aoc.io.text2subsets(input)
    parser = algo1(data[0])["0"]
    result = []
    for line in data[1]:
        result.append(re.fullmatch(parser, line))
    result = [x != None for x in result]
    logger.info(result)
    return sum(result)


def task2(input):
    data = aoc.io.text2subsets(input)
    parser = algo1(data[0])
    result = []
    prefix = parser["42"]
    suffix1 = parser["42"]
    suffix2 = parser["31"]
    logger.info(prefix)
    logger.info(suffix1)
    logger.info(suffix2)

    for line in data[1]:
        logger.info(line)
        # result.append(re.fullmatch(new_parser, line))
        for i in range(1, len(line) - 1):
            found = 0
            split1 = line[:i]
            split2 = line[i:]
            match1 = re.fullmatch(f"({prefix})+", split1)
            if not match1:
                continue
            logger.info(match1.group(0))
            suffix_parser = ""
            for j in range(0, len(split2) // 2):
                suffix_parser = f"({suffix1})({suffix_parser})({suffix2})"
                match2 = re.fullmatch(suffix_parser, split2)
                if match2:
                    logger.info(match2.group(0))
                    found = 1
                    logger.error(line)
                    result.append(line)
                    break
            if found:
                break
        # finds = re.findall(prefix, line)

    logger.info(result)
    return len(result)


if __name__ == "__main__":
    data = open("day19_input.txt").read().strip()
    # result1 = task(data)
    # logger.info(result1)
    result2 = task2(data)
    logger.info(result2)
