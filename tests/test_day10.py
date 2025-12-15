import pytest

from advent_of_code_25 import day10


@pytest.fixture
def example_input() -> str:
    return (
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n"
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n"
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    )


@pytest.fixture
def example_machines(example_input: str) -> list[day10.Machine]:
    return [
        day10.Machine.from_text(line) for line in example_input.strip().splitlines()
    ]


def test_machine_from_text(example_input: str):
    machines = [
        day10.Machine.from_text(line) for line in example_input.strip().splitlines()
    ]

    assert len(machines[0].desired_state) == 4
    assert len(machines[1].desired_state) == 5
    assert len(machines[2].desired_state) == 6

    assert len(machines[0].buttons) == 6
    assert len(machines[1].buttons) == 5
    assert len(machines[2].buttons) == 4

    assert len(machines[0].joltages) == 4
    assert len(machines[1].joltages) == 5
    assert len(machines[2].joltages) == 6


def test_machine_get_starting_state(example_machines: list[day10.Machine]):
    states = [machine.get_starting_state() for machine in example_machines]

    assert states == [
        (False, False, False, False),
        (False, False, False, False, False),
        (False, False, False, False, False, False),
    ]


def test_get_button_state_change(example_machines: list[day10.Machine]):
    # Machine 1
    state = example_machines[0].get_starting_state()
    state = day10.get_button_state_change(state, example_machines[0].buttons[0])
    state = day10.get_button_state_change(state, example_machines[0].buttons[1])
    state = day10.get_button_state_change(state, example_machines[0].buttons[2])
    assert state == example_machines[0].desired_state

    state = example_machines[0].get_starting_state()
    state = day10.get_button_state_change(state, example_machines[0].buttons[1])
    state = day10.get_button_state_change(state, example_machines[0].buttons[3])
    state = day10.get_button_state_change(state, example_machines[0].buttons[5])
    state = day10.get_button_state_change(state, example_machines[0].buttons[5])
    assert state == example_machines[0].desired_state

    state = example_machines[0].get_starting_state()
    state = day10.get_button_state_change(state, example_machines[0].buttons[0])
    state = day10.get_button_state_change(state, example_machines[0].buttons[2])
    state = day10.get_button_state_change(state, example_machines[0].buttons[3])
    state = day10.get_button_state_change(state, example_machines[0].buttons[4])
    state = day10.get_button_state_change(state, example_machines[0].buttons[5])
    assert state == example_machines[0].desired_state

    state = example_machines[0].get_starting_state()
    state = day10.get_button_state_change(state, example_machines[0].buttons[4])
    state = day10.get_button_state_change(state, example_machines[0].buttons[5])
    assert state == example_machines[0].desired_state

    # Machine 2
    state = example_machines[1].get_starting_state()
    state = day10.get_button_state_change(state, example_machines[1].buttons[2])
    state = day10.get_button_state_change(state, example_machines[1].buttons[3])
    state = day10.get_button_state_change(state, example_machines[1].buttons[4])
    assert state == example_machines[1].desired_state

    # Machine 3
    state = example_machines[2].get_starting_state()
    state = day10.get_button_state_change(state, example_machines[2].buttons[1])
    state = day10.get_button_state_change(state, example_machines[2].buttons[2])
    assert state == example_machines[2].desired_state


def test_get_minimum_button_presses(example_machines: list[day10.Machine]):
    presses = [machine.get_minimum_button_presses() for machine in example_machines]

    assert presses == [2, 3, 2]


def test_get_minimum_button_presses_joltages(example_machines: list[day10.Machine]):
    presses = [
        machine.get_minimum_button_presses_joltages() for machine in example_machines
    ]

    assert presses == [10, 12, 11]
