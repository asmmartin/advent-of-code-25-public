"""https://adventofcode.com/2025/day/04"""

import sys
from time import perf_counter

ROLL = "@"


def rolls_from_text(text: str) -> set[complex]:
    rolls = set()

    for y, line in enumerate(text.strip().splitlines()):
        for x, tile in enumerate(line.strip()):
            if tile == ROLL:
                rolls.add(y * 1j + x)
    return rolls


def find_accessibles_by_forklift(rolls: set[complex]) -> set[complex]:
    deltas = (-1j, +1j, -1, +1, 1j + 1, 1j - 1, -1j + 1, -1j - 1)

    accesibles = set()
    for roll in rolls:
        neighbours = 0
        for delta in deltas:
            if roll + delta in rolls:
                neighbours += 1
        if neighbours < 4:
            accesibles.add(roll)

    return accesibles


def find_all_removables_by_forklift(rolls: set[complex]) -> set[complex]:
    removables = set()

    while True:
        accesibles = find_accessibles_by_forklift(rolls)
        if not accesibles:
            return removables
        removables.update(accesibles)
        rolls -= accesibles


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    rolls = rolls_from_text(input_text)
    accesibles = find_accessibles_by_forklift(rolls)
    solution_1 = len(accesibles)

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    removables = find_all_removables_by_forklift(rolls)
    solution_2 = len(removables)

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
