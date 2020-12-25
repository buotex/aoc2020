import numpy as np
from collections import defaultdict


def lines2dict(data):
    data_dict = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            data_dict[(i, j)] = char
    return data_dict


def text2dict(data):
    data = text2subsets(data)
    data_dict = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            data_dict[(i, j)] = char
    return data_dict


def dict2text(data):
    max_i = max(data.keys(), key=lambda x: x[0])[0]
    max_j = max(data.keys(), key=lambda x: x[1])[1]
    result = []
    for i in range(max_i + 1):
        line = []
        for j in range(max_j + 1):
            line.append(data[(i, j)])
        result.append("".join(line))
    return "\n".join(result)


def text2grid(data, mapping=lambda x: x):
    data = list(map(lambda x: [mapping(i) for i in x], data))
    # data = np.array([mapping[letter]  for row in data for letter in row])
    return np.array(data)


def grid2dict(data, default=0):
    data_dict = defaultdict(int)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            data_dict[(i, j)] = data[i, j]

    return data_dict


def dict2grid(data, shape):
    new_data = np.zeros(shape)
    for key, value in data.items():
        new_data[key[0], key[1]] = value
    return new_data


def grid2text(data, mapping=lambda x: x):
    result = []
    for row in data:
        result.append("".join([mapping(entry) for entry in row]))
    return "\n".join(result)


def text2subsets(input: str, algo=lambda x: x, *, join_lines=False):
    """
    Args:
        join_lines (bool): If True, do string concatenation on subset and turn result into string
    """
    data = [line.strip() for line in input.strip().split("\n")]
    subsets = []
    subset = []
    for line in data:
        if line == "":
            if join_lines == True:
                subset = " ".join(subset)
            subsets.append(subset)
            subset = []
        else:
            subset.append(line)
    if join_lines == True:
        subset = " ".join(subset)
    subsets.append(subset)
    if len(subsets) == 1:
        subsets = subsets[0]
    return list(map(algo, subsets))
