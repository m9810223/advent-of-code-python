def cast_input(inputs: str):
    # A for Rock, B for Paper, and C for Scissors - your opponent
    # X for Rock, Y for Paper, and Z for Scissors - you
    return [list(map(ord, x.split())) for x in inputs.splitlines()]


N = 3
A, X = ord("A"), ord("X")

SHIFT = N - X % N


def _score_shape(x):
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    return x - X + 1


def _score_outcome(a, x):  # outcome: 0, 1, 2 -> score: 0, 3, 6
    return (((x - a) + SHIFT) % N) * N


def part1(inputs):
    def score(a, x):
        return _score_shape(x) + _score_outcome(a, x)

    return sum(score(*x) for x in inputs)


def _choose_shape(a, e):
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    return X + (a + A + e % N) % N


def part2(inputs):
    def score(a, x):
        s = _choose_shape(a, x)
        return _score_shape(s) + _score_outcome(a, s)

    return sum(score(*x) for x in inputs)
