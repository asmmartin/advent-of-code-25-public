"""https://adventofcode.com/2025/day/07"""

import sys
from dataclasses import dataclass
from functools import cache
from time import perf_counter

START = "S"
SPLITTER = "^"


@dataclass(frozen=True)
class Manifold:
    splitters: frozenset[complex]
    start: complex
    width: int
    height: int

    @classmethod
    def from_text(cls, text: str) -> Manifold:
        splitters = set()
        start = None

        lines = text.strip().splitlines()
        for y, line in enumerate(lines):
            for x, tile in enumerate(line.strip()):
                if tile == START:
                    start = y * 1j + x
                elif tile == SPLITTER:
                    splitters.add(y * 1j + x)

        if start is None:
            raise ValueError("There is no start!")

        return cls(
            splitters=frozenset(splitters),
            start=start,
            width=len(lines[0]),
            height=len(lines),
        )

    def get_hit_splitters(self) -> set[complex]:
        hit_splitters: set[complex] = set()

        beams_in_level: list[set[complex]] = [set((self.start,))]

        for y in range(self.height - 1):
            beams_in_level.append(set())
            for x in range(self.width):
                coords = y * 1j + x
                if coords not in beams_in_level[y]:
                    continue
                if (coords + 1j) in self.splitters:
                    hit_splitters.add(coords + 1)
                    beams_in_level[y + 1].add(coords + 1j + 1)
                    beams_in_level[y + 1].add(coords + 1j - 1)
                else:
                    beams_in_level[y + 1].add(coords + 1j)

        return hit_splitters

    @cache
    def count_timelines(self, coords: None | complex = None) -> int:
        coords = coords if coords is not None else self.start

        while int(coords.imag) < self.height:
            if coords in self.splitters:
                return self.count_timelines(coords + 1) + self.count_timelines(
                    coords - 1
                )

            coords += 1j
        return 1


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    manifold = Manifold.from_text(input_text)
    hit_splitters = manifold.get_hit_splitters()
    solution_1 = len(hit_splitters)
    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    timelines_count = manifold.count_timelines()
    solution_2 = timelines_count

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
