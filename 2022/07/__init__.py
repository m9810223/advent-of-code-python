import functools
from pprint import pformat
from typing import Literal


def cast_input(inputs: str):
    def parse_ls(line: str):
        info, name = line.split()
        return info if info == 'dir' else int(info), name

    def parse_output(output: str):
        if not output:
            return []

        return list(map(parse_ls, filter(bool, output.split('\n'))))

    def parse_interactivity(interactivity: str):
        in_, out = interactivity.split('\n', maxsplit=1)
        return in_, parse_output(out)

    return list(map(parse_interactivity, filter(bool, inputs.split('$ '))))


class Pwd:
    def __init__(self):
        self._pwd: list[str] = []

    def cd(self, d: str):
        if d != '..':
            return self._pwd.append(d)

        self._pwd.pop()

    @property
    def curr(self):
        return self._pwd[1:]


class Dir:
    def __init__(self):
        self.dirs: dict[str, Dir] = {}
        self.files: dict[str, int] = {}

    def read_ls(self, pwd: list[str], infos: list[tuple[int | Literal['dir'], str]]):
        if pwd:
            p, *ps = pwd
            self.dirs[p].read_ls(ps, infos)
            return

        for info, name in infos:
            if info == 'dir':
                self.dirs[name] = Dir()
                continue
            self.files[name] = info

    @property
    @functools.cache
    def size(self):
        s = sum(self.files.values())
        return s + sum(d.size for d in self.dirs.values())  # type: ignore

    def size_at_most(self, n: int):
        s = self.size if self.size <= n else 0
        return s + sum(d.size_at_most(n) for d in self.dirs.values())

    def __repr__(self):
        return pformat(self.files | self.dirs)


def create_root(inputs: list[tuple[str, list[tuple[int | Literal['dir'], str]]]]):
    root = Dir()
    pwd = Pwd()
    for in_, out in inputs:
        if in_.startswith('cd '):
            cd, d = in_.split(maxsplit=1)
            pwd.cd(d)
            continue
        root.read_ls(pwd.curr, out)
    return root


def part1(inputs):
    return create_root(inputs).size_at_most(100000)


def part2(inputs):
    root = create_root(inputs)
    result = root.size
    target_size = 30000000 - (70000000 - root.size)
    q = root.dirs.values()
    while q:  # bfs
        n = []
        for d in q:
            size = d.size
            if size >= target_size:
                result = min(result, size)
            n.extend(d.dirs.values())
        q = n
    return result
