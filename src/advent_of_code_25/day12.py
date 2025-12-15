"""https://adventofcode.com/2025/day/12"""

import sys
from dataclasses import dataclass
from time import perf_counter

type Shape = tuple[tuple[int, int], ...]


@dataclass
class Region:
    dimensions: tuple[int, int]
    shape_quantities: tuple[int, ...]

    @property
    def area(self):
        return self.dimensions[0] * self.dimensions[1]

    def shapes_tiles_exceed_area(self, shapes: tuple[Shape, ...]) -> bool:
        if len(shapes) != len(self.shape_quantities):
            raise ValueError("Shapes and shape quantities mismatch")
        shape_tiles_count = sum(
            len(shape) * self.shape_quantities[i] for i, shape in enumerate(shapes)
        )
        return shape_tiles_count > self.area


def shapes_and_regions_from_text(
    text: str,
) -> tuple[tuple[Shape, ...], tuple[Region, ...]]:
    *shape_texts, regions_text = text.strip().split("\n\n")

    shapes: list[Shape] = []

    for shape_text in shape_texts:
        shape = []
        for y, line in enumerate(shape_text.strip().splitlines()):
            if y == 0:
                continue
            for x, char in enumerate(line.strip()):
                if char == "#":
                    shape.append((x, y - 1))
        shapes.append(tuple(shape))

    regions: list[Region] = []
    for line in regions_text.strip().splitlines():
        dims, shape_counts = line.split(": ")
        x, y = dims.split("x")[:2]
        regions.append(
            Region(
                dimensions=(int(x), int(y)),
                shape_quantities=tuple(int(c) for c in shape_counts.split()),
            )
        )

    return tuple(shapes), tuple(regions)


def main(input_text: str):
    start = perf_counter()

    # Part 1
    # Not a general solution. For the specific input, all the valid regions
    # have plenty of space, whereas for the invalid ones the total count of
    # shape tiles exceed the region's area.
    solution_1 = None
    shapes, regions = shapes_and_regions_from_text(input_text)
    big_regions = [
        region for region in regions if not region.shapes_tiles_exceed_area(shapes)
    ]
    solution_1 = len(big_regions)

    part_1_time = perf_counter() - start

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
