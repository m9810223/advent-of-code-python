def cast_input(inputs: str):
    return [list(map(int, x)) for x in inputs.splitlines()]


def sight(I: int, J: int, i: int, j: int, di: int, dj: int):
    """
    top    -> di,dj = -1, 0
    left   -> di,dj =  0,-1
    bottom -> di,dj =  1, 0
    right  -> di,dj =  0, 1
    """
    steps = min([I, I - i, i + 1][di], [J, J - j, j + 1][dj])
    return ((i + s * di, j + s * dj) for s in range(steps))


DIRECTIONS = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]


def part1(inputs: list[list[int]]):
    I, J = len(inputs), len(inputs[0])

    def visible(i: int, j: int, di: int, dj: int):
        line = sight(I, J, i, j, di, dj)
        fi, fj = next(line)
        return all(inputs[curr_i][curr_j] < inputs[fi][fj] for curr_i, curr_j in line)

    return sum(any(visible(i, j, *d) for d in DIRECTIONS) for i in range(I) for j in range(J))


def mul(it):
    result = 1
    for n in it:
        result *= n
    return result


def part2(inputs: list[list[int]]):
    I, J = len(inputs), len(inputs[0])

    def score(i: int, j: int, di: int, dj: int):
        line = sight(I, J, i, j, di, dj)
        fi, fj = next(line)
        result = 0
        for curr_i, curr_j in line:
            result += 1
            if inputs[curr_i][curr_j] >= inputs[fi][fj]:
                break
        return result

    def scenic_score(i: int, j: int):
        return mul(score(i, j, *d) for d in DIRECTIONS)

    return max(scenic_score(i, j) for i in range(I) for j in range(J))
