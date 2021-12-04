# 🎄 Advent-of-code-python ⭐

Advent of code Python solutions and CLI tool.

<details>

<summary>2021</summary>

|  2021   | Puzzle Name       | Part 1 | Part 2 |
| :-----: | :---------------- | :----: | :----: |
| Day🎄01 | Sonar Sweep       |   ⭐   |   ⭐   |
| Day🎄02 | Dive!             |   ⭐   |   ⭐   |
| Day🎄03 | Binary Diagnostic |   ⭐   |   ⭐   |
| Day🎄04 |                   |        |        |
| Day🎄05 |                   |        |        |
| Day🎄06 |                   |        |        |
| Day🎄07 |                   |        |        |
| Day🎄08 |                   |        |        |
| Day🎄09 |                   |        |        |
| Day🎄10 |                   |        |        |
| Day🎄11 |                   |        |        |
| Day🎄12 |                   |        |        |
| Day🎄13 |                   |        |        |
| Day🎄14 |                   |        |        |
| Day🎄15 |                   |        |        |
| Day🎄16 |                   |        |        |
| Day🎄17 |                   |        |        |
| Day🎄18 |                   |        |        |
| Day🎄19 |                   |        |        |
| Day🎄20 |                   |        |        |
| Day🎄21 |                   |        |        |
| Day🎄22 |                   |        |        |
| Day🎄23 |                   |        |        |
| Day🎄24 |                   |        |        |
| Day🎄25 |                   |        |        |

</details>

---

# CLI

## setup

```
$ poetry install
$ poetry shell
```

## run latest day

```
$ aoc_run.py
2021.03
  2021.03.part1: 2640986
    (100, 1): (0.296106 sec, 0.003089 sec) 
  2021.03.trie_part2: 6822109
    (100, 1): (0.527668 sec, 0.007096 sec) 
```

## run single day/part

```
$ aoc_run.py [-y year] [day] [part]
```

## run all

```
$ aoc_run.py all
2021.01
  2021.01.old_part1: 1655
    (100, 1): (0.010870 sec, 0.000137 sec) 
  2021.01.part1: 1655
    (100, 1): (0.019144 sec, 0.000193 sec) 
  2021.01.part2: 1683
    (100, 1): (0.018879 sec, 0.000193 sec) 
2021.02
  2021.02.part1: 1561344
    (100, 1): (0.008623 sec, 0.000087 sec) 
  2021.02.part2: 1848454425
    (100, 1): (0.011373 sec, 0.000118 sec) 
```

# Example

[`=> 2021/01/__init__.py`](2021/01/__init__.py)

# Create files:

```
mkdir -p ${year}/${day}
touch $_/{__init__.py,input}
```

## input data

save input data to `part${part}.input` files.

## coding

edit `${year}/${day}/__init__.py`:

Create function name `cast_input` to cast inputs.

```python
# shared
def cast_input(inputs):
    return [
        x for x in inputs.split('\n')
    ]
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
