# 🎄 Advent-of-code-python ⭐

A Python CLI tool for adventofcode.

---

# Setup

```
$ poetry install
$ poetry shell
```

# CLI

## run latest day

```
$ python adventofcode.py run
```

## run single day/part

```
$ python adventofcode.py run [-y year] [day] [part]
```

# Example

[`=> 2021/01/__init__.py`](2021/01/__init__.py)

# Output

```
$ python adventofcode.py run
<module '2021.01' from 'adventofcode/2021/01/__init__.py'>
________________________________________________________________________________
<function old_part1 at 0x7f02b36400d0>
(1k, 1) -> (0.11475160000009055, 0.0001143000008596573)
output = 1655
________________________________________________________________________________
<function part1 at 0x7f02b3640940>
(1k, 1) -> (0.1937553999996453, 0.00019330000031914096)
output = 1655
________________________________________________________________________________
<function part2 at 0x7f02b3640160>
(1k, 1) -> (0.19324570000026142, 0.00019149999934597872)
output = 1683

```

# Create files:

```
mkdir -p ${year}/${day}
touch $_/{__init__.py,{part1,part2}.input}
```

## input data

save input data to `part${part}.input` files.

## coding

edit `${year}/${day}/__init__.py`:

Create function name `cast_input` or `part${part}_cast_input` to cast inputs.

```python
# shared
def cast_input(line):
    d, v = line.split()
    return d, int(v)


# separated
def part1_cast_input(line):
    return int(line)
def part2_cast_input(line):
    return int(line)
```

Create function to solve puzzle -- function name ends with `part1` or `part2`

```python
def old_part1(inputs):
    ...


def part1(inputs):
    ...


def part2(inputs):
    ...

```

---

|  2021   | Part 1 | Part 2 |
| :-----: | :----: | :----: |
| Day🎄01 |   ⭐   |   ⭐   |
| Day🎄02 |   ⭐   |   ⭐   |
| Day🎄03 |        |        |
| Day🎄04 |        |        |
| Day🎄05 |        |        |
| Day🎄06 |        |        |
| Day🎄07 |        |        |
| Day🎄08 |        |        |
| Day🎄09 |        |        |
| Day🎄10 |        |        |
| Day🎄11 |        |        |
| Day🎄12 |        |        |
| Day🎄13 |        |        |
| Day🎄14 |        |        |
| Day🎄15 |        |        |
| Day🎄16 |        |        |
| Day🎄17 |        |        |
| Day🎄18 |        |        |
| Day🎄19 |        |        |
| Day🎄20 |        |        |
| Day🎄21 |        |        |
| Day🎄22 |        |        |
| Day🎄23 |        |        |
| Day🎄24 |        |        |
| Day🎄25 |        |        |
