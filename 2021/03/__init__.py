def cast_input(line):
    return line


def part1(inputs):
    l = len(inputs[0])
    gamma = [0]*l
    for line in inputs:
        for i in range(l):
            gamma[i] += (-1)**(line[i] == '0')
    gamma = int(''.join(str(int(x > 0)) for x in gamma), 2)
    return gamma*(2**l-1-gamma)


def trie_part2(inputs):
    root = {'len': 0, 'childs': []}
    for line in inputs:
        curr = root
        for char in line:
            curr = curr.setdefault(int(char), {'len': 0, 'childs': []})
            curr['len'] += 1
            curr['childs'].append(line)

    def find(root, oxygen=True):
        if root['len'] == 1:
            return root['childs'][0]
        if oxygen:
            if root[1]['len'] >= root[0]['len']:
                return find(root[1], oxygen)
            return find(root[0], oxygen)
        if root[0]['len'] <= root[1]['len']:
            return find(root[0], oxygen)
        return find(root[1], oxygen)

    oxygen = int(find(root), 2)
    CO2 = int(find(root, False), 2)

    return oxygen*CO2
