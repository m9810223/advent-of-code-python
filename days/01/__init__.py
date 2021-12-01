def old_s1(input_):
    prev = int(input_[0])
    res = 0
    for v in input_[1:]:
        v = int(v)
        if v > prev:
            res += 1
        prev = v
    return res


def s2(input_, offset=3):
    res = 0
    for i in range(offset):
        input_[i] = int(input_[i])
    for i in range(len(input_)-offset):
        input_[i+offset] = int(input_[i+offset])
        if input_[i+offset] > input_[i]:
            res += 1
    return res


def s1(input_):
    return s2(input_, offset=1)
