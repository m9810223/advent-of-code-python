def cast_input(inputs):
    return [[int(x) for l in line.split(" -> ") for x in l.split(",")] for line in inputs.split("\n")]


def new_part1(inputs):
    dx, dy = {}, {}
    for x1, y1, x2, y2 in inputs:
        if x1 == x2:
            l, g = (y1, y2) if y1 < y2 else (y2, y1)
            t = dx[x1] = dx.get(x1, {})
            t[l] = t.get(l, 0) + 1
            t[g + 1] = t.get(g + 1, 0) - 1
        elif y1 == y2:
            l, g = (x1, x2) if x1 < x2 else (x2, x1)
            t = dy[y1] = dy.get(y1, {})
            t[l] = t.get(l, 0) + 1
            t[g + 1] = t.get(g + 1, 0) - 1

    res = {}
    for x, d in dx.items():
        acc = 0
        for y in range(1 + max(d.keys())):
            acc += d.get(y, 0)
            res[(x, y)] = res.get((x, y), 0) + acc
    for y, d in dy.items():
        acc = 0
        for x in range(1 + max(d.keys())):
            acc += d.get(x, 0)
            res[(x, y)] = res.get((x, y), 0) + acc

    return len([x for x in res.values() if x > 1])


def naive_part1(inputs):
    res = {}
    for x1, y1, x2, y2 in inputs:
        if x1 == x2:
            l, g = (y1, y2) if y1 < y2 else (y2, y1)
            for y in range(l, g + 1):
                res[(x1, y)] = res.get((x1, y), 0) + 1
        elif y1 == y2:
            l, g = (x1, x2) if x1 < x2 else (x2, x1)
            for x in range(l, g + 1):
                res[(x, y1)] = res.get((x, y1), 0) + 1
    return len([x for x in res.values() if x > 1])


def naive_part2(inputs):
    res = {}
    for x1, y1, x2, y2 in inputs:
        if x1 == x2:
            l, g = (y1, y2) if y1 < y2 else (y2, y1)
            for y in range(l, g + 1):
                res[(x1, y)] = res.get((x1, y), 0) + 1
        elif y1 == y2:
            l, g = (x1, x2) if x1 < x2 else (x2, x1)
            for x in range(l, g + 1):
                res[(x, y1)] = res.get((x, y1), 0) + 1
        else:
            dx = x2 - x1
            dy = y2 - y1
            a = abs(dx)
            if a != abs(dy):
                continue
            ix = 1 if x2 > x1 else -1
            iy = 1 if y2 > y1 else -1
            x, y = x1, y1
            for _ in range(a + 1):
                res[(x, y)] = res.get((x, y), 0) + 1
                x += ix
                y += iy
    return len([x for x in res.values() if x > 1])
