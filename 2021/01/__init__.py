def cast_input(inputs):
    return [int(x) for x in inputs.split("\n")]


def old_part1(inputs):
    prev = inputs[0]
    res = 0
    for v in inputs[1:]:
        if v > prev:
            res += 1
        prev = v
    return res


def part2(inputs, offset=3):
    res = 0
    for i in range(len(inputs) - offset):
        if inputs[i + offset] > inputs[i]:
            res += 1
    return res


def part1(inputs):
    return part2(inputs, offset=1)
