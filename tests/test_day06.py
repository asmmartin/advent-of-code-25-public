import operator

import pytest

from advent_of_code_25 import day06


@pytest.fixture
def example_input() -> str:
    return "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "


@pytest.fixture
def example_problems() -> list[day06.Problem]:
    return day06.problems_from_text(
        "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
    )


def test_problems_from_text(example_input):
    problems = day06.problems_from_text(example_input)

    assert len(problems) == 4

    assert all(len(problem.operands) == 3 for problem in problems)
    assert [problem.operation for problem in problems] == [
        operator.mul,
        operator.add,
        operator.mul,
        operator.add,
    ]


def test_problem_solve(example_problems):
    solutions = [p.solve() for p in example_problems]

    assert solutions == [33210, 490, 4243455, 401]


def test_problems_from_cephalopod_text(example_input):
    problems = day06.problems_from_cephalopod_text(example_input)

    assert len(problems) == 4

    assert all(len(problem.operands) == 3 for problem in problems)
    assert [problem.operation for problem in problems] == [
        operator.add,
        operator.mul,
        operator.add,
        operator.mul,
    ]

    assert [p.solve() for p in problems] == [1058, 3253600, 625, 8544]
