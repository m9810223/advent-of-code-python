from pprint import pprint


def cast_input(inputs):
    return [[part.split() for part in line.split(" | ")] for line in inputs.split("\n")]


def part1(inputs):
    res = 0
    for _, a in inputs:
        res += len([x for x in a if len(x) in (2, 3, 4, 7)])
    return res


{
    1: 2,  # *   c  f
    # _        0010010
    7: 3,  # * a c  f
    # _        1010010
    4: 4,  # *  bcd f
    # _        0111010
    2: 5,  # _ a cde g
    3: 5,  # _ a cd fg
    5: 5,  # _ ab d fg
    # _        3123123
    0: 6,  # _ abc efg
    6: 6,  # _ ab defg
    9: 6,  # _ abcd fg
    # _        3322233
}
l_map = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

c_map = {
    "01033": "a",
    "00113": "b",
    "11122": "c",
    "00132": "d",
    "00012": "e",
    "11123": "f",
    "00033": "g",
}


def gen_dic(b, a):
    dic = {}
    pprint(b)
    for x in b:
        l = len(x)
        for c in x:
            dic[c] = dic.get(c, [0] * 8)
            dic[c][l] += 1

    print(dic)


def part2(inputs):
    ...
    for b, a in inputs:
        _ = gen_dic(b, a)
        exit()
