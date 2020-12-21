import numpy as np
import pandas as pd
import io
import re
import sys
import itertools
import functools
from collections import defaultdict

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
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
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
    assert task(testdata) == "mxmxvkd,sqjhc,fvjkl"


def task(input):
    data = aoc.io.text2subsets(input)
    all_ingredients = []
    all_allergens = []

    for line in data:
        ingredients, allergens = line.split("(")
        print(ingredients)
        ingredients = re.findall(r"\w+", ingredients)
        allergens = re.findall(r"\w+", allergens)[1:]
        all_ingredients.append(ingredients)
        all_allergens.append(allergens)
    # data = list(map(subfunc, data))
    all_existing_allergens = set(itertools.chain(*all_allergens))
    logger.info(all_existing_allergens)
    all_existing_ingredients = set(itertools.chain(*all_ingredients))
    mapping = {
        allergen: all_existing_ingredients for allergen in all_existing_allergens
    }

    for ingredients, allergens in zip(all_ingredients, all_allergens):
        for allergen in allergens:
            mapping[allergen] = mapping[allergen].intersection(set(ingredients))
    remaining_ingredients = set(itertools.chain(*mapping.values()))
    unused_ingredients = all_existing_ingredients.difference(remaining_ingredients)
    counts = defaultdict(int)
    for ingredient in unused_ingredients:
        for ingredients in all_ingredients:
            if ingredient in ingredients:
                counts[ingredient] += 1

    logger.info(remaining_ingredients)
    final_mapping = {}

    for _ in range(len(mapping.keys())):
        logger.info(final_mapping)
        for allergen, ingredients in mapping.items():
            if allergen in final_mapping:
                continue
            logger.info(allergen)
            logger.info(ingredients)
            if len(ingredients) == 1:
                logger.info(allergen)
                logger.info(ingredients)
                ingredient = list(ingredients)[0]
                final_mapping[allergen] = ingredient
                # throw it away from all others
                found_mapping = (allergen, ingredient)
                break
        for allergen, ingredients in mapping.items():
            if allergen != found_mapping[0]:
                logger.info(mapping)
                logger.info(ingredients)
                logger.info(found_mapping[1])
                try:
                    ingredients.remove(found_mapping[1])
                except:
                    pass
                logger.info(ingredients)
                mapping[allergen] = ingredients
    sorted_allergens = sorted(final_mapping.keys())
    result = [final_mapping[key] for key in sorted_allergens]

    return ",".join(result)

    # return sum(counts.values())


if __name__ == "__main__":
    data = open("day21_input.txt").read().strip()
    result1 = task(data)
    logger.info(result1)
    # result2 = task2(data)
    # logger.info(result2)
