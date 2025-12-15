"""https://adventofcode.com/2025/day/09"""

import sys
from itertools import combinations
from time import perf_counter
from typing import Iterable

import shapely
import shapely.prepared

type Tile = tuple[int, int]


def tiles_from_text(text: str) -> list[Tile]:
    tiles = []
    for line in text.strip().splitlines():
        a, b = line.split(",")
        tiles.append((int(a), int(b)))

    return tiles


def calculate_area(a: Tile, b: Tile) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def find_largest_area(tiles: Iterable[Tile]) -> int:
    pairs = combinations(tiles, 2)
    areas = [calculate_area(a, b) for a, b in pairs]
    return max(areas)


def find_largest_area_restricted(tiles: list[Tile]) -> int:
    pairs = combinations(tiles, 2)
    rectangles = [(calculate_area(a, b), (a, b)) for a, b in pairs]
    rectangles.sort(reverse=True)

    # First approach
    # For every rectangle candidate:
    #   - Validate it does not intersect with any poligon side
    #   (using AABB 2D collision detection)
    #   - Validate its center is inside the poligon (with ray casting or
    #   winding number algorithms), to handle concavities
    # That is too much hassle (specially second check). Easier to use shapely

    polygon = shapely.prepared.prep(shapely.Polygon(tiles))

    for area, (p1, p2) in rectangles:
        box = shapely.box(
            min(p1[0], p2[0]),
            min(p1[1], p2[1]),
            max(p1[0], p2[0]),
            max(p1[1], p2[1]),
        )
        if polygon.contains(box):
            # As they are sorted by area, the first match is the biggest
            return area
    return 0


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    tiles = tiles_from_text(input_text)
    largest_area = find_largest_area(tiles)
    solution_1 = largest_area

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    restricted_largest_area = find_largest_area_restricted(tiles)
    solution_2 = restricted_largest_area

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
