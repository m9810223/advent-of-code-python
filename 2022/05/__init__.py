def _parse_crates(inputs: str):
    def split(s: str, n=4):
        return [s[i : i + n][1].strip() for i in range(0, len(s), n)]

    crates = list(map(split, inputs.splitlines()[:-1]))
    crates: list[list[str]] = list(map(list, zip(*crates[::-1])))
    return [list(filter(bool, x)) for x in crates]


def _parse_procedure(inputs: str):
    def parse(moving: str):
        m = moving.split(" ")
        return list(map(int, (m[i] for i in range(1, len(m), 2))))

    return list(map(parse, inputs.splitlines()))


def cast_input(inputs: str):
    crates, procedure = inputs.split("\n" * 2)
    return _parse_crates(crates), _parse_procedure(procedure)


def crane(crates: list[list[str]], move: int, from_: int, to: int):
    [crates[to - 1].append(crates[from_ - 1].pop()) for _ in range(move)]


def part1(inputs: tuple[list[list[str]], list[list[int]]]):
    crates, procedure = inputs
    [crane(crates, *x) for x in procedure]
    return "".join([x[-1] for x in crates])


def crane9001(crates: list[list[str]], move: int, from_: int, to: int):
    stack = []
    [stack.append(crates[from_ - 1].pop()) for _ in range(move)]
    [crates[to - 1].append(stack.pop()) for _ in range(move)]


def part2(inputs: tuple[list[list[str]], list[list[int]]]):
    crates, procedure = inputs
    [crane9001(crates, *x) for x in procedure]
    return "".join([x[-1] for x in crates])
