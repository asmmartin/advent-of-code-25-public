import pytest

from advent_of_code_25 import day04


@pytest.fixture
def example_input() -> str:
    return (
        "..@@.@@@@.\n"
        "@@@.@.@.@@\n"
        "@@@@@.@.@@\n"
        "@.@@@@..@.\n"
        "@@.@@@@.@@\n"
        ".@@@@@@@.@\n"
        ".@.@.@.@@@\n"
        "@.@@@.@@@@\n"
        ".@@@@@@@@.\n"
        "@.@.@@@.@."
    )


@pytest.fixture
def example_rolls() -> set[complex]:
    return day04.rolls_from_text(
        "..@@.@@@@.\n"
        "@@@.@.@.@@\n"
        "@@@@@.@.@@\n"
        "@.@@@@..@.\n"
        "@@.@@@@.@@\n"
        ".@@@@@@@.@\n"
        ".@.@.@.@@@\n"
        "@.@@@.@@@@\n"
        ".@@@@@@@@.\n"
        "@.@.@@@.@."
    )


def test_rolls_from_text(example_input: str):
    rolls = day04.rolls_from_text(example_input)

    assert len(rolls) == 71


def test_find_accessibles_by_forklift(example_rolls: set[complex]):
    accesible = day04.find_accessibles_by_forklift(example_rolls)

    assert len(accesible) == 13


def test_find_all_removables_by_forklift(example_rolls: set[complex]):
    removable = day04.find_all_removables_by_forklift(example_rolls)

    assert len(removable) == 43
