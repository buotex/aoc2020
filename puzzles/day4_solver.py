import numpy as np
import pandas as pd
import io
import re
import sys
from loguru import logger
from pytest import fixture

import aoc

logger.remove()
logger.add(sys.stderr, format="{level} {name}:{function}:{line} {message}")

@fixture()
def testdata():
    return """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm

    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929

    hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

    hcl:#cga07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in"""

testdata2 = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022

    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

def test_inputs(testdata):
    testdata = testdata.split("\n")
    assert func(testdata) == 2


def is_valid(passport):
    if ("byr" in passport and
            "iyr" in passport and 
            "eyr" in passport and
            "hgt" in passport and
            "hcl" in passport and
            "ecl" in passport and
            "pid" in passport
            ):
        return True
    return False

def is_valid_long(passport):
    is_valid = True
    if ("byr" in passport and
            len(passport["byr"]) == 4 and
            int(passport["byr"]) >= 1920 and
            int(passport["byr"]) <= 2002
            ):
        is_valid &= True
    else:
        is_valid = False

    if ("iyr" in passport and
            len(passport["iyr"]) == 4 and
            int(passport["iyr"]) >= 2010 and
            int(passport["iyr"]) <= 2020
            ):
        is_valid &= True
    else:
        is_valid = False

    if ("eyr" in passport and
            len(passport["eyr"]) == 4 and
            int(passport["eyr"]) >= 2020 and
            int(passport["eyr"]) <= 2030):
        is_valid &= True
    else:
        is_valid = False

    if ("hgt" in passport):
        match = re.fullmatch("([0-9]+)(cm|in)", passport["hgt"])
        if match:
            if match.group(2) == "cm":
                if int(match.group(1)) >= 150 and int(match.group(1)) <= 193:
                    is_valid &= True
                else:
                    is_valid = False
            elif match.group(2) == "in":
                if int(match.group(1)) >= 59 and int(match.group(1)) <= 76:
                    is_valid &= True
                else:
                    is_valid = False
            else:
                is_valid = False
        else:
            is_valid = False
    else:
        is_valid = False

    if ("hcl" in passport):
        is_valid &= (re.fullmatch("#[0-9abcdef]{6}", passport["hcl"]) is not None)
    else:
        is_valid = False

    if ("ecl" in passport):
        is_valid &= passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]
    else:
        is_valid = False

    if ("pid" in passport):
        is_valid &= (re.fullmatch("[0-9]{9}", passport["pid"]) is not None)
    else:
        is_valid = False
            
    return is_valid

def func(input, validator = is_valid_long):
    counter = 0
    passport = {}
    for line in input:
        tokens = line.split()
        if len(tokens) == 0:
            # empty line
            #print(passport)
            if validator(passport):
                counter += 1
                if "cid" in passport:
                    del passport["cid"]
                print([passport[key] for key in sorted(passport)])
            passport = {}
            continue
        for x in tokens:
            key, value = x.split(":")
            passport[key] = value
    return counter

if __name__ == "__main__":
    testdata = testdata.split("\n")
    testdata2 = testdata2.split("\n")
    data = [line.rstrip() for line in open("day4_input.txt")]
    #print(data)
    #print(func(testdata2))
    print(func(data))
