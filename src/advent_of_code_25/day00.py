"""https://adventofcode.com/2025/day/00"""

import sys
from time import perf_counter


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
