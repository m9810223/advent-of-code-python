# 🎄 Advent-of-code-python ⭐

Advent of code Python solutions and CLI tool.

<!-- <details> -->

<!-- <summary>2022</summary> -->

|  2022   | Puzzle Name             | Part 1 | Part 2 |
| :-----: | :---------------------- | :----: | :----: |
| Day🎄01 | Calorie Counting        |   ⭐   |   ⭐   |
| Day🎄02 | Rock Paper Scissors     |   ⭐   |   ⭐   |
| Day🎄03 | Rucksack Reorganization |   ⭐   |   ⭐   |
| Day🎄04 | Camp Cleanup            |   ⭐   |   ⭐   |
| Day🎄05 |                         |        |        |
| Day🎄06 |                         |        |        |
| Day🎄07 |                         |        |        |
| Day🎄08 |                         |        |        |
| Day🎄09 |                         |        |        |
| Day🎄10 |                         |        |        |
| Day🎄11 |                         |        |        |
| Day🎄12 |                         |        |        |
| Day🎄13 |                         |        |        |
| Day🎄14 |                         |        |        |
| Day🎄15 |                         |        |        |
| Day🎄16 |                         |        |        |
| Day🎄17 |                         |        |        |
| Day🎄18 |                         |        |        |
| Day🎄19 |                         |        |        |
| Day🎄20 |                         |        |        |
| Day🎄21 |                         |        |        |
| Day🎄22 |                         |        |        |
| Day🎄23 |                         |        |        |
| Day🎄24 |                         |        |        |
| Day🎄25 |                         |        |        |

<!-- </details> -->

<details>

<summary>2021</summary>

|  2021   | Puzzle Name          | Part 1 | Part 2 |
| :-----: | :------------------- | :----: | :----: |
| Day🎄01 | Sonar Sweep          |   ⭐   |   ⭐   |
| Day🎄02 | Dive!                |   ⭐   |   ⭐   |
| Day🎄03 | Binary Diagnostic    |   ⭐   |   ⭐   |
| Day🎄04 | Giant Squid          |   ⭐   |   ⭐   |
| Day🎄05 | Hydrothermal Venture |   ⭐   |   ⭐   |
| Day🎄06 | Lanternfish          |   ⭐   |   ⭐   |
| Day🎄07 |                      |        |        |
| Day🎄08 |                      |        |        |
| Day🎄09 |                      |        |        |
| Day🎄10 |                      |        |        |
| Day🎄11 |                      |        |        |
| Day🎄12 |                      |        |        |
| Day🎄13 |                      |        |        |
| Day🎄14 |                      |        |        |
| Day🎄15 |                      |        |        |
| Day🎄16 |                      |        |        |
| Day🎄17 |                      |        |        |
| Day🎄18 |                      |        |        |
| Day🎄19 |                      |        |        |
| Day🎄20 |                      |        |        |
| Day🎄21 |                      |        |        |
| Day🎄22 |                      |        |        |
| Day🎄23 |                      |        |        |
| Day🎄24 |                      |        |        |
| Day🎄25 |                      |        |        |

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
  part-1
    ƒ part1
      0.190877 2640986
  part-2
    ƒ trie_part2
      0.335679 6822109
```

## run single day/part

```
$ aoc_run.py [-y year] [day] [part]
```

## run all

```
$ aoc_run.py all
2021.01
  part-1
    ƒ old_part1
      0.007498 1655
    ƒ part1
      0.013324 1655
  part-2
    ƒ part2
      0.012959 1683

2021.02
  part-1
    ƒ part1
      0.005937 1561344
  part-2
    ƒ part2
      0.007568 1848454425

2021.03
  part-1
    ƒ part1
      0.190877 2640986
  part-2
    ƒ trie_part2
      0.335679 6822109
```

# Example

[`=> 2021/01/__init__.py`](2021/01/__init__.py)

# Create files:

`mkdir -p ${year}/${day} && touch $_/{__init__.py,input}`

## input data

save input data to `input` files.

## coding

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
