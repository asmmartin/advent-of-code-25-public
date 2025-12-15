import pytest

from advent_of_code_25 import day07


@pytest.fixture
def example_input() -> str:
    return (
        ".......S.......\n"
        "...............\n"
        ".......^.......\n"
        "...............\n"
        "......^.^......\n"
        "...............\n"
        ".....^.^.^.....\n"
        "...............\n"
        "....^.^...^....\n"
        "...............\n"
        "...^.^...^.^...\n"
        "...............\n"
        "..^...^.....^..\n"
        "...............\n"
        ".^.^.^.^.^...^.\n"
        "..............."
    )


@pytest.fixture
def example_manifold(example_input: str) -> day07.Manifold:
    return day07.Manifold.from_text(example_input)


@pytest.fixture
def example_simple_manifold(example_input: str) -> day07.Manifold:
    return day07.Manifold.from_text(
        "\n".join(
            (
                "..S..",
                "..^..",
                ".....",
                ".^.^.",
                ".....",
            )
        )
    )


def test_manifold_from_text(example_input: str):
    board = day07.Manifold.from_text(example_input)

    assert len(board.splitters) == 22
    assert board.start == 7
    assert board.width == 15
    assert board.height == 16


def test_manifold_get_hit_splitters(example_manifold: day07.Manifold):
    hit_splitters = example_manifold.get_hit_splitters()

    assert len(hit_splitters) == 21


def test_manifold_count_timelines_simple(example_simple_manifold: day07.Manifold):
    timelines_count = example_simple_manifold.count_timelines()

    assert timelines_count == 4


def test_manifold_count_timelines(example_manifold: day07.Manifold):
    timelines_count = example_manifold.count_timelines()

    assert timelines_count == 40
