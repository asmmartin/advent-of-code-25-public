"""https://adventofcode.com/2025/day/10"""

import heapq
import re
import sys
from dataclasses import dataclass
from time import perf_counter

import numpy as np
from scipy.optimize import linprog

type Button = tuple[int, ...]
type State = tuple[bool, ...]


@dataclass
class Machine:
    desired_state: State
    buttons: tuple[Button, ...]
    joltages: tuple[int, ...]

    @classmethod
    def from_text(cls, text: str) -> Machine:
        lights_match = re.search(r"\[(.*?)\]", text)
        if not lights_match:
            raise ValueError("Invalid input text")
        desired_state = tuple(light == "#" for light in lights_match.group(1))

        buttons = tuple(
            tuple(map(int, button_text.split(",")))
            for button_text in re.findall(r"\(([^()]+?)\)", text)
        )

        joltages_text = re.search(r"\{([^}]*)\}", text)
        if not joltages_text:
            raise ValueError("Invalid input text")
        joltages = tuple(map(int, joltages_text.group(1).split(",")))

        return cls(
            desired_state=desired_state,
            buttons=buttons,
            joltages=joltages,
        )

    def get_starting_state(self) -> State:
        return (False,) * len(self.desired_state)

    def get_minimum_button_presses(self) -> int:
        seen_states = set()
        queue = [(0, self.get_starting_state())]

        while queue:
            presses, state = heapq.heappop(queue)
            if state == self.desired_state:
                return presses

            presses += 1
            for button in self.buttons:
                next_state = get_button_state_change(state, button)
                if next_state in seen_states:
                    continue
                seen_states.add(next_state)
                heapq.heappush(queue, (presses, next_state))

        raise RuntimeError("unreachable")

    def get_minimum_button_presses_joltages(self) -> int:
        M = len(self.joltages)
        N = len(self.buttons)

        matrix = [np.zeros(N) for _ in range(M)]
        for j, button in enumerate(self.buttons):
            for light in button:
                matrix[light][j] = 1

        c = np.ones(N)
        bounds = [(0, None)] * N

        result = linprog(
            c=c,
            A_eq=matrix,
            b_eq=self.joltages,
            bounds=bounds,
            integrality=1,
        )
        if not result.success:
            raise RuntimeError("There is no solution")

        # Fix float rounding errors
        presses = [round(x) if np.isclose(x, round(x)) else x for x in result.x]

        return sum(presses)


def get_button_state_change(state: State, button: Button) -> State:
    next_state = list(state)
    for light_index in button:
        next_state[light_index] = not next_state[light_index]
    return tuple(next_state)


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    machines = [Machine.from_text(line) for line in input_text.strip().splitlines()]
    presses = [machine.get_minimum_button_presses() for machine in machines]
    solution_1 = sum(presses)

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    presses = [machine.get_minimum_button_presses_joltages() for machine in machines]
    solution_2 = sum(presses)

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
