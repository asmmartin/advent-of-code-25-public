import pytest

from advent_of_code_25 import day05


@pytest.fixture
def example_input() -> str:
    return "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"


@pytest.fixture
def example_database() -> day05.Database:
    return day05.Database.from_text("3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32")


def test_database_from_text(example_input: str):
    database = day05.Database.from_text(example_input)

    assert len(database.fresh_ranges) == 2
    assert len(database.ingredients) == 6


def test_database_find_fresh(example_database: day05.Database):
    fresh = example_database.find_fresh()

    assert fresh == {5, 11, 17}


def test_database_count_possible_fresh_ids(example_database: day05.Database):
    possible_fresh_count = example_database.count_possible_fresh_ids()

    assert possible_fresh_count == 14
