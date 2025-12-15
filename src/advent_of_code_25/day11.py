"""https://adventofcode.com/2025/day/11"""

import sys
from dataclasses import dataclass
from functools import cache
from time import perf_counter


@dataclass
class Connections:
    conns: dict[str, list[str]]

    @classmethod
    def from_text(cls, text: str) -> Connections:
        connections: dict[str, list[str]] = {}
        for line in text.strip().splitlines():
            key, outs = line.strip().split(":")
            connections[key.strip()] = outs.split()

        connections["out"] = []
        return cls(connections)

    def __hash__(self):
        return id(self)

    @cache
    def count_paths(self, start: str = "you", end: str = "out") -> int:
        if start == end:
            return 1

        # Assume no cycles
        path_count = sum(self.count_paths(out, end) for out in self.conns[start])

        return path_count


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    connections = Connections.from_text(input_text)
    path_count = connections.count_paths("you")
    solution_1 = path_count

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    svr_dac = connections.count_paths("svr", "dac")
    dac_fft = connections.count_paths("dac", "fft")
    fft_out = connections.count_paths("fft", "out")

    svr_fft = connections.count_paths("svr", "fft")
    fft_dac = connections.count_paths("fft", "dac")
    dac_out = connections.count_paths("dac", "out")

    result = (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out)
    solution_2 = result

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
