"""https://adventofcode.com/2025/day/01"""

import sys
from dataclasses import dataclass
from time import perf_counter
from typing import Iterable, Self


@dataclass
class Rotation:
    direction: str
    clicks: int

    @classmethod
    def from_text(cls, text: str) -> Self:
        return cls(direction=text[0], clicks=int(text[1:]))

    def __repr__(self) -> str:
        return f"{self.direction}{self.clicks}"


def password_from_rotations(rotations: Iterable[Rotation]) -> int:
    dial = 50
    zero_count = 0

    for rotation in rotations:
        if rotation.direction == "R":
            dial = (dial + rotation.clicks) % 100
        elif rotation.direction == "L":
            dial = (dial - rotation.clicks) % 100
        else:
            raise ValueError(f"Invalid direction {rotation.direction!r}")
        if dial == 0:
            zero_count += 1

    return zero_count


def move_dial(dial: int, rotation: Rotation) -> tuple[int, int]:
    if rotation.clicks == 0:
        return dial, 0

    prev_dial = dial

    if rotation.direction == "R":
        zeroes, dial = divmod(dial + rotation.clicks, 100)
    elif rotation.direction == "L":
        zeroes, dial = divmod(dial - rotation.clicks, 100)
        zeroes = abs(zeroes)

        if prev_dial == 0 and dial > 0:
            zeroes -= 1
        elif prev_dial > 0 and dial == 0:
            zeroes += 1
    else:
        raise ValueError(f"Invalid direction {rotation.direction!r}")

    return dial, zeroes


def password_CLICK_from_rotations(rotations: Iterable[Rotation]) -> int:
    dial = 50
    zero_count = 0

    for rotation in rotations:
        dial, zeroes = move_dial(dial, rotation)
        zero_count += zeroes
    return zero_count


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    rotations = tuple(
        Rotation.from_text(line) for line in input_text.strip().splitlines()
    )
    password = password_from_rotations(rotations)
    solution_1 = password

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    password = password_CLICK_from_rotations(rotations)
    solution_2 = password

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
