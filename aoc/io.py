


def text2subsets(input, algo):
    data = [line.rstrip() for line in input.split("\n")]
    subsets = []
    subset = []
    for line in data:
        if line == "":
            subsets.append(subset)
            subset = []
        else:
            subset.append(line)
    subsets.append(subset)
    return list(map(algo, subsets))

