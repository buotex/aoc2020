import numpy as np


def text2grid(data, mapping=lambda x: x):
    data = list(map(lambda x: [mapping[i] for i in x], data))
    #data = np.array([mapping[letter]  for row in data for letter in row])
    return np.array(data)


def grid2text(data, mapping=lambda x: x):
    result = []
    for row in data:
        result.append("".join([mapping[entry] for entry in row]))
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

