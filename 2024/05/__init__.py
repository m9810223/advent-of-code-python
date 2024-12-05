def cast_input(inputs: str):
    a, b = map(str.splitlines, inputs.split("\n\n"))
    rules = [tuple(map(int, x.split("|"))) for x in a]
    updates = [list(map(int, x.split(","))) for x in b]
    return rules, updates


def part1(
    inputs: tuple[
        list[tuple[int, int]],
        list[list[int]],
    ],
):
    rules, updates = inputs

    d: dict[int, list[int]] = {}
    for x, y in rules:
        d[x] = d.get(x, [])
        d[x].append(y)

    print(d)


def part2(inputs):
    pass
