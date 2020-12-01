import numpy as np
import pandas as pd

import aoc2020

data = pd.read_csv("./day1_input.txt", names=["entry"], dtype=[("entry", "int")])
print(data.info())
data_list = data.entry.to_numpy()
summed = data_list + data_list[:, np.newaxis]
mult = data_list * data_list[:, np.newaxis]
print(mult[summed == 2020])
summed = data_list + data_list[:, np.newaxis]
triple_sum = summed.reshape(-1) + data_list[:, np.newaxis]

mult = data_list * data_list[:, np.newaxis]
triple_mult = mult.reshape(-1) * data_list[:, np.newaxis]
print(triple_mult[triple_sum == 2020])
