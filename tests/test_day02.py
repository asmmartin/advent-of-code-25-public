from typing import Iterable

import pytest

from advent_of_code_25 import day02


@pytest.fixture
def example_input() -> str:
    return (
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
        "824824821-824824827,2121212118-2121212124"
    )


@pytest.fixture
def example_ranges(example_input: str) -> Iterable[range]:
    return day02.ranges_from_text(example_input)


def test_ranges_from_text(example_input: str):
    ranges = day02.ranges_from_text(example_input)

    assert len(ranges) == 11
    assert all(type(r) == range for r in ranges)


def test_get_invalid_ids(example_ranges: Iterable[range]):
    invalid_ids = [day02.get_invalid_ids(r) for r in example_ranges]

    assert invalid_ids == [
        {11, 22},
        {99},
        {1010},
        {1188511885},
        {222222},
        set(),
        {446446},
        {38593859},
        set(),
        set(),
        set(),
    ]

    assert sum(sum(ids) for ids in invalid_ids) == 1227775554

    assert day02.get_invalid_ids(range(3, 12)) == {11}
    assert 1010 in day02.get_invalid_ids(range(123, 1013))


def test_get_invalid_ids_multiple(example_ranges: Iterable[range]):
    invalid_ids = [day02.get_invalid_ids_multiple(r) for r in example_ranges]

    assert invalid_ids == [
        {11, 22},
        {99, 111},
        {999, 1010},
        {1188511885},
        {222222},
        set(),
        {446446},
        {38593859},
        {565656},
        {824824824},
        {2121212121},
    ]

    assert sum(sum(ids) for ids in invalid_ids) == 4174379265
