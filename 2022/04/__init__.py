def cast_input(inputs: str):
    return map(
        lambda x: map(lambda x: map(int, str(x).split('-')), str(x).split(',')),
        inputs.splitlines(),
    )


def fully_contains(x):
    (al, ar), (bl, br) = x
    return al <= bl and br <= ar or al >= bl and br >= ar


def part1(inputs):
    return sum(map(fully_contains, inputs))


def overlap(x):
    (al, ar), (bl, br) = x
    return max(al, bl) <= min(ar, br)


def part2(inputs):
    return sum(map(overlap, inputs))
