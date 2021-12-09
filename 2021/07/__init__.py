def cast_input(inputs):
    return [
        int(string)
        for string in inputs.split(',')
    ]


def median_part1(inputs):
    inputs = sorted(inputs)
    l = len(inputs)
    h = l // 2
    if l % 2:
        m = inputs[h]
    else:
        m = (inputs[h] + inputs[h-1])//2

    res = 0
    for x in inputs:
        res += abs(m-x)
    return res


def naive_part1(inputs):
    res = min(
        sum(abs(x-i) for x in inputs)
        for i in range(min(inputs), 1+max(inputs))
    )
    raise RuntimeError(f'{res}, slow')


def f(x):
    return (1+x)*x//2


def naive_part2(inputs):
    inputs = sorted(inputs)
    res = float('inf')
    for i in range(min(inputs), 1+max(inputs)):
        new = sum(
            f(abs(i-x))
            for x in inputs
        )
        if new < res:
            res = new
            continue
        raise RuntimeError(f'{res}, slow')


def average_part2(inputs):
    # not proved that the ans between [average.floor, average.ceil]
    inputs = sorted(inputs)
    average = sum(inputs) // len(inputs)
    return min(
        sum(
            f(abs(average+y-x)) for x in inputs
        )
        for y in range(2)
    )


"""
notes (not proved)

for sorted X:

2f(k) = -sum_(1,k)_(Xi) + sum_(k+1,n)_(Xi) + n(Xk^2) + (n^2+2k)Xk + n(n+1)(2n+1)/6
2[f(k)-f(k+1)] = n(Xk^2-X_(k+1)^2) + (n^2+2k)(Xk-X_(k+1))
"""
