def cast_input(inputs):
    return [int(string) for string in inputs.split(',')]


class Lanternfish:
    def __init__(self, time=8):
        self.time = time

    def count_down(self):
        if self.time:
            self.time -= 1
            return
        self.time = 6
        return True  # spawn

    def __repr__(self):
        return f'{self.time}'


def naive_oo_part1(inputs):
    days = 80
    fishes = [Lanternfish(x) for x in inputs]
    for _ in range(days):
        new_fishes = []
        for fish in fishes:
            if fish.count_down():
                new_fishes.append(Lanternfish())
        fishes.extend(new_fishes)
    res = len(fishes)
    raise RuntimeError(f'{res}, slow')


def cache_recur_part1(inputs, days=80):
    cache = {}

    def f(time, day):
        if (time, day) in cache:
            return cache[(time, day)]
        if not day > 0:
            res = 1
        elif time == 0:
            res = f(6, day - 1) + f(8, day - 1)
        else:
            res = f(time - 1, day - 1)
        cache[(time, day)] = res
        return res

    return sum(f(x, days) for x in inputs)


def cache_recur_part2(inputs):
    return cache_recur_part1(inputs, 256)
