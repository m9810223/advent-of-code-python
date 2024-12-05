import collections


def cast_input(inputs):
    return inputs


def detect(inputs: str, n: int):
    string = " " + inputs
    c = collections.Counter(string[:n])
    for i in range(n, len(string)):
        c.subtract([string[i - n]]), c.update([string[i]])
        if all(map(lambda x: x <= 1, c.values())):
            return i


def part1(inputs):
    return detect(inputs, 4)


def part2(inputs):
    return detect(inputs, 14)
