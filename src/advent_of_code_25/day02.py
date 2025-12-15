"""https://adventofcode.com/2025/day/02"""

import re
import sys
from time import perf_counter


def ranges_from_text(text: str) -> tuple[range, ...]:
    parts = text.strip().split(",")

    ranges = []
    for part in parts:
        start, end = part.split("-")
        ranges.append(range(int(start), int(end) + 1))
    return tuple(ranges)


def get_invalid_ids(r: range) -> set[int]:
    invalid_ids = set()

    if len(str(r.start)) == len(str(r.stop - 1)) and len(str(r.start)) % 2:
        return invalid_ids

    s = str(r.start)
    half = int(s[: len(s) // 2] or 0)

    while (to_check := int(f"{half}{half}")) < r.stop:
        to_check = int(f"{half}{half}")

        if to_check >= r.stop:
            break
        if to_check in r:
            invalid_ids.add(to_check)

        half += 1

    return invalid_ids


def get_invalid_ids_multiple(r: range) -> set[int]:
    pattern = re.compile(r"^(.+)\1+$")

    invalid_ids = set()
    # Bruteforce feasible. Input with less than 1e6 numbers per range, 35 ranges.
    for number in r:
        if pattern.match(str(number)):
            invalid_ids.add(number)

    return invalid_ids


def main(input_text: str):
    start = perf_counter()

    # Part 1
    ranges = ranges_from_text(input_text)
    invalid_ids = [get_invalid_ids(r) for r in ranges]
    solution_1 = sum(sum(ids) for ids in invalid_ids)

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    invalid_ids = [get_invalid_ids_multiple(r) for r in ranges]
    solution_2 = sum(sum(ids) for ids in invalid_ids)

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
