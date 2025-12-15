import pytest

from advent_of_code_25 import day03

assert day03


@pytest.fixture
def example_input() -> str:
    return "987654321111111\n811111111111119\n234234234234278\n818181911112111"


def test_find_max_joltage(example_input: str):
    banks = example_input.splitlines()
    max_joltages = [day03.find_max_joltage(bank) for bank in banks]

    assert max_joltages == [98, 89, 78, 92]


def test_find_max_joltage_long(example_input: str):
    banks = example_input.splitlines()
    max_joltages = [day03.find_max_joltage_long(bank) for bank in banks]

    assert max_joltages == [987654321111, 811111111119, 434234234278, 888911112111]
