import pandas as pd
import numpy as np
import operator
from itertools import *

def text2np(data, mapping=lambda x: x):
    data = list(map(lambda x: [mapping[i] for i in x], data))
    #data = np.array([mapping[letter]  for row in data for letter in row])
    return np.array(data)


def np2text(data, mapping=lambda x: x):
    result = []
    for row in data:
        result.append("".join([mapping[entry] for entry in row]))
    return "\n".join(result)
