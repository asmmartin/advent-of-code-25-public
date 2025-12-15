import pytest

from advent_of_code_25 import day09


@pytest.fixture
def example_input() -> str:
    return "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3"


@pytest.fixture
def example_input_edge_case() -> str:
    return "1,0\n3,0\n3,6\n16,6\n16,0\n18,0\n18,9\n13,9\n13,7\n6,7\n6,9\n1,9"


def test_tiles_from_text(example_input: str):
    tiles = day09.tiles_from_text(example_input)

    assert len(tiles) == 8
    assert all(len(t) == 2 for t in tiles)


def test_calculate_area():
    areas = [
        day09.calculate_area((2, 5), (9, 7)),
        day09.calculate_area((7, 1), (11, 7)),
        day09.calculate_area((7, 3), (2, 3)),
        day09.calculate_area((2, 5), (11, 1)),
    ]

    assert areas == [24, 35, 6, 50]


def test_find_largest_area(example_input: str):
    tiles = day09.tiles_from_text(example_input)
    largest_area = day09.find_largest_area(tiles)

    assert largest_area == 50


def test_find_largest_area_restricted(example_input: str):
    tiles = day09.tiles_from_text(example_input)
    largest_area_restricted = day09.find_largest_area_restricted(tiles)

    assert largest_area_restricted == 24


def test_find_largest_area_restricted_edge_case(example_input_edge_case: str):
    tiles = day09.tiles_from_text(example_input_edge_case)
    largest_area_restricted = day09.find_largest_area_restricted(tiles)

    assert largest_area_restricted == 30
