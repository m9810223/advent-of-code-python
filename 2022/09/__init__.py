DIRECTIONS: dict[str, tuple[int, int]] = {
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1),
}


def cast_input(inputs: str):
    return [(DIRECTIONS[x[0]], int(x[1])) for x in map(str.split, inputs.splitlines())]


def follow(t: tuple[int, int], h: tuple[int, int]):
    (hi, hj), (ti, tj) = h, t
    shape = ((hi - ti) ** 2) + ((hj - tj) ** 2)
    if shape == 4:
        return (hi + ti) // 2, (hj + tj) // 2
    if shape in [5, 8]:
        return (
            (hi + ti) // 2 if abs(hi - ti) == 2 else hi,
            (hj + tj) // 2 if abs(hj - tj) == 2 else hj,
        )
    return t


def move(h: tuple[int, int], d: tuple[int, int]):
    (hi, hj), (di, dj) = h, d
    return hi + di, hj + dj


def part1(inputs: list[tuple[tuple[int, int], int]]):
    head = tail = (0, 0)
    positions: set[tuple[int, int]] = {tail}
    for d, a in inputs:
        for _ in range(a):
            head = move(head, d)
            tail = follow(tail, head)
            positions.add(tail)
    return len(positions)


def part2(inputs: list[tuple[tuple[int, int], int]]):
    N = 10
    knots: list[tuple[int, int]] = [(0, 0) for _ in range(N)]
    positions: set[tuple[int, int]] = {knots[-1]}
    for d, a in inputs:
        for _ in range(a):
            knots[0] = move(knots[0], d)
            for i in range(1, N):
                knots[i] = follow(knots[i], knots[i - 1])
            positions.add(knots[-1])
    return len(positions)
