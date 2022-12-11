def cast_input(inputs: str):
    results: list[tuple[int, int]] = []
    for line in inputs.splitlines():
        if line == 'noop':
            results.append((1, 0))
        elif line.startswith('addx '):
            results.append((2, int(line.rsplit(maxsplit=1).pop())))
    return results


def part1(inputs: list[tuple[int, int]]):
    result = 0
    cycle, value = 1, 1
    for c, x in inputs:
        for v in [0] * (c - 1) + [x]:
            value += v
            cycle += 1
            if cycle % 40 == 20:
                result += cycle * value
    return result


def render(c: list[str], wide: int, letters: int):
    def split(seq, amt: int):
        return [seq[i : i + amt] for i in range(0, len(seq), amt)]

    lines = ((' ' * 3).join(split(x, wide // letters)) for x in split(''.join(c), wide))
    return '\n' + '\n'.join(lines)


def part2(inputs: list[tuple[int, int]]):
    RADIUS = 3 // 2  # the sprite is 3 pixels wide
    WIDE, HIGH, LETTERS = 40, 6, 8
    LIT, DARK = '#.'
    crt = [LIT] * (WIDE * HIGH)
    cycle, value = 1, 1
    for c, x in inputs:
        for v in [0] * (c - 1) + [x]:
            value += v
            if abs(value - cycle % WIDE) > RADIUS:
                crt[cycle] = DARK
            cycle += 1
            if cycle == WIDE * HIGH:
                return render(crt, WIDE, LETTERS)
