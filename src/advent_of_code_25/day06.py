"""https://adventofcode.com/2025/day/06"""

import operator
import sys
from dataclasses import dataclass
from functools import reduce
from time import perf_counter
from typing import Callable

OPERATIONS = {
    "+": operator.add,
    "*": operator.mul,
}


@dataclass
class Problem:
    operands: list[int]
    operation: Callable[[int, int], int]

    def solve(self) -> int:
        return reduce(self.operation, self.operands)


def problems_from_text(text: str) -> list[Problem]:
    lines = [line.split() for line in text.strip().splitlines()]
    problems: list[Problem] = []
    for c in range(len(lines[0])):
        operands = [int(line[c]) for line in lines[:-1]]
        problems.append(Problem(operands=operands, operation=OPERATIONS[lines[-1][c]]))
    return problems


def problems_from_cephalopod_text(text: str) -> list[Problem]:
    lines = text.splitlines()
    lines = [" " + line for line in lines]

    # Check same amount of columns
    if len({len(line) for line in lines}) > 1:
        raise ValueError("Columns number not consistent!")

    problems: list[Problem] = []

    operands: list[int] = []
    operation: Callable[[int, int], int] | None = None
    for c in range(len(lines[0]) - 1, -1, -1):
        if (op_symbol := lines[-1][c]) != " ":
            operation = OPERATIONS[op_symbol]

        operand_str = "".join(line[c] for line in lines[:-1])
        if not operand_str.strip():
            if operation is None:
                raise ValueError("End of problem without operation")
            problems.append(Problem(operands, operation))
            operands = []
            operation = None
        else:
            operands.append(int(operand_str))

    return problems


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    problems = problems_from_text(input_text)
    solutions = [p.solve() for p in problems]
    solution_1 = sum(solutions)

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    problems = problems_from_cephalopod_text(input_text)
    solutions = [p.solve() for p in problems]
    solution_2 = sum(solutions)

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
