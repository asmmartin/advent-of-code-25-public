"""https://adventofcode.com/2025/day/03"""

import sys
from time import perf_counter


def find_max_joltage(bank: str) -> int:
    joltages = tuple(int(b) for b in bank)
    first = joltages.index(max(joltages[:-1]))
    second = joltages.index(max(joltages[first + 1 :]))

    return joltages[first] * 10 + joltages[second]


def find_max_joltage_long(bank: str) -> int:
    SIZE = 12

    # Edge case does not apply based on the input
    if len(bank) < SIZE:
        raise NotImplementedError(f"Edge case not implemented: bank length < {SIZE}")

    joltages = tuple(int(b) for b in bank)
    max_joltages = [0] * SIZE

    for joltage in joltages:
        max_joltages.append(joltage)
        for i in range(SIZE):
            if max_joltages[i] < max_joltages[i + 1]:
                max_joltages.pop(i)
                break
        else:
            max_joltages.pop(-1)

    return int("".join(str(d) for d in max_joltages))


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    banks = input_text.splitlines()
    max_joltages = [find_max_joltage(bank) for bank in banks]
    solution_1 = sum(max_joltages)

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    long_max_joltages = [find_max_joltage_long(bank) for bank in banks]
    solution_2 = sum(long_max_joltages)

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
