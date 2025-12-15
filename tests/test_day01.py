import pytest

from advent_of_code_25 import day01


@pytest.fixture
def example_input() -> str:
    return "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"


@pytest.fixture
def example_rotations(example_input: str) -> tuple[day01.Rotation, ...]:
    return tuple(
        day01.Rotation.from_text(line) for line in example_input.strip().splitlines()
    )


def test_rotations_from_input(example_input: str):
    rotations = [
        day01.Rotation.from_text(line) for line in example_input.strip().splitlines()
    ]


def test_password_from_rotations(example_rotations: tuple[day01.Rotation, ...]):
    password = day01.password_from_rotations(example_rotations)

    assert password == 3


def test_move_dial(example_rotations: tuple[day01.Rotation, ...]):
    assert day01.move_dial(0, day01.Rotation("R", 0)) == (0, 0)
    assert day01.move_dial(0, day01.Rotation("R", 100)) == (0, 1)
    assert day01.move_dial(50, day01.Rotation("R", 1)) == (51, 0)
    assert day01.move_dial(50, day01.Rotation("R", 51)) == (1, 1)
    assert day01.move_dial(50, day01.Rotation("R", 851)) == (1, 9)
    assert day01.move_dial(50, day01.Rotation("R", 50)) == (0, 1)

    assert day01.move_dial(0, day01.Rotation("L", 0)) == (0, 0)
    assert day01.move_dial(50, day01.Rotation("L", 1)) == (49, 0)
    assert day01.move_dial(50, day01.Rotation("L", 51)) == (99, 1)
    assert day01.move_dial(50, day01.Rotation("L", 851)) == (99, 9)
    assert day01.move_dial(50, day01.Rotation("L", 50)) == (0, 1)
    assert day01.move_dial(0, day01.Rotation("L", 50)) == (50, 0)


def test_password_CLICK_from_rotations(example_rotations: tuple[day01.Rotation, ...]):
    password = day01.password_CLICK_from_rotations(example_rotations)

    assert password == 6
