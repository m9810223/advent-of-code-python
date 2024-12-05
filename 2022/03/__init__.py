from functools import reduce


def cast_input(inputs: str):
    return inputs.splitlines()


LOWERCASE, UPPERCASE = ord("a") - 1, ord("A") - 1


def convert(char):
    o = ord(char)
    return o - LOWERCASE if o > LOWERCASE else o - UPPERCASE + 26


def rearrange(rucksack):
    half = len(rucksack) // 2
    return rucksack[:half], rucksack[half:]


def part1(inputs):
    def both(a, b):
        return convert(next(iter(set(a) & set(b))))

    return sum(both(a, b) for a, b in map(rearrange, inputs))


def group(items, n: int):
    return [items[i : i + n] for i in range(0, len(items), n)]


def common(x):
    return next(iter(reduce(lambda a, b: set(a) & set(b), x)))


def mmap(funcs, iterable):
    return reduce(lambda fx, fy: map(fy, fx), funcs, iterable)


def part2(inputs):
    return sum(mmap([common, convert], group(inputs, 3)))


def new_part1(inputs):
    return sum(mmap([rearrange, common, convert], inputs))
