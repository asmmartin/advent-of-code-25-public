"""https://adventofcode.com/2025/day/05"""

import sys
from dataclasses import dataclass
from time import perf_counter
from typing import Iterable


@dataclass
class Database:
    fresh_ranges: tuple[range, ...]
    ingredients: tuple[int, ...]

    @classmethod
    def from_text(cls, text: str) -> Database:
        ranges_part, ids_part = text.strip().split("\n\n")

        ranges: list[range] = []
        for r in ranges_part.strip().splitlines():
            start, end = r.strip().split("-")
            ranges.append(range(int(start), int(end) + 1))
        ids = tuple(int(i) for i in ids_part.strip().splitlines())

        return cls(
            fresh_ranges=merge_ranges(tuple(ranges)),
            ingredients=ids,
        )

    def find_fresh(self) -> set[int]:
        return {
            ingredient
            for ingredient in self.ingredients
            if any(ingredient in r for r in self.fresh_ranges)
        }

    def count_possible_fresh_ids(self) -> int:
        return sum(len(r) for r in self.fresh_ranges)


def merge_ranges(ranges: Iterable[range]) -> tuple[range, ...]:
    ranges = sorted(ranges, key=lambda r: (r.start, r.stop))

    merged: list[range] = []
    for i, rng in enumerate(ranges):
        is_already_merged = bool(merged and merged[-1].stop >= rng.stop)
        if is_already_merged:
            continue

        # Find stop
        stop = rng.stop
        for next_range in ranges[i + 1 : len(ranges)]:
            if next_range.start <= stop:
                stop = max(stop, next_range.stop)

        merged.append(range(rng.start, stop))

    return tuple(merged)


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    database = Database.from_text(input_text)
    fresh = database.find_fresh()
    solution_1 = len(fresh)

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    solution_2 = database.count_possible_fresh_ids()

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
