import numpy as np
import pandas as pd

import aoc

#data_list = data.entry.to_numpy()
#summed = data_list + data_list[:, np.newaxis]
#mult = data_list * data_list[:, np.newaxis]
#print(mult[summed == 2020])
#summed = data_list + data_list[:, np.newaxis]
#triple_sum = summed.reshape(-1) + data_list[:, np.newaxis]
#
#mult = data_list * data_list[:, np.newaxis]
#triple_mult = mult.reshape(-1) * data_list[:, np.newaxis]
#print(triple_mult[triple_sum == 2020])

def func(input):
    data = np.array(aoc.io.text2subsets(input, int))
    summed = data + data[:, np.newaxis]
    mult = data * data[:, np.newaxis]
    return mult[summed == 2020]

def func2(input):
    data = np.array(aoc.io.text2subsets(input, int))
    mult = data * data[:, np.newaxis]
    summed = data + data[:, np.newaxis]
    triple_sum = summed.reshape(-1) + data[:, np.newaxis]
    triple_mult = mult.reshape(-1) * data[:, np.newaxis]
    return triple_mult[triple_sum == 2020]


if __name__ == "__main__":
    #data = [line.rstrip() for line in open("dayx_input.txt").read()]
    data = open("day1_input.txt").read().strip()
    print(func(data))
    print(func2(data))
