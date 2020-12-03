import pandas as pd
import numpy as np

def text2int(data, mapping):
    data = data.transform(lambda x: np.array([mapping[letter] for letter in x], dtype="int8"))
    data = np.vstack(data.to_numpy())
    return data


def int2text(data, mapping):
    result = []
    for row in data:
        result.append("".join([mapping[entry] for entry in row]))
    return "\n".join(result)
