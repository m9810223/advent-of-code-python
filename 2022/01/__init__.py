def cast_input(inputs: str):
    return [int(x) if x else None for x in inputs.splitlines()]


def part1(inputs):
    result = 0
    acc = 0
    for calory in inputs:
        if calory is None:
            result = max(result, acc)
            acc = 0
        else:
            acc += calory
    return result


class Top:
    def __init__(self, k: int = 1):
        self._k = k
        self._top = [0] * k  # left > right

    def push(self, val: int):
        self._top.append(val)
        for i in range(self._k - 1, -1, -1):
            if self._top[i] >= self._top[i + 1]:
                break
            self._top[i : i + 2] = self._top[i + 1], self._top[i]
        self._top.pop()

    @property
    def top(self):
        return self._top[: self._k]


def part2(inputs):
    t = Top(3)
    acc = 0
    for calory in inputs:
        if calory is None:
            t.push(acc)
            acc = 0
            continue
        acc += calory
    t.push(acc)
    return sum(t.top)


def new_part1(inputs):
    t = Top(1)
    acc = 0
    for calory in inputs:
        if calory is None:
            t.push(acc)
            acc = 0
            continue
        acc += calory
    t.push(acc)
    return sum(t.top)
