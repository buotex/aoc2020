import fileinput
if __name__ == '__main__':
    lines = [*fileinput.input()]
    print(lines)
