import pytest

from advent_of_code_25 import day12


@pytest.fixture
def example_input() -> str:
    return (
        "0:\n"
        "###\n"
        "##.\n"
        "##.\n"
        "\n"
        "1:\n"
        "###\n"
        "##.\n"
        ".##\n"
        "\n"
        "2:\n"
        ".##\n"
        "###\n"
        "##.\n"
        "\n"
        "3:\n"
        "##.\n"
        "###\n"
        "##.\n"
        "\n"
        "4:\n"
        "###\n"
        "#..\n"
        "###\n"
        "\n"
        "5:\n"
        "###\n"
        ".#.\n"
        "###\n"
        "\n"
        "4x4: 0 0 0 0 2 0\n"
        "12x5: 1 0 1 0 2 2\n"
        "12x5: 1 0 1 0 3 2"
    )


def test_shapes_and_regions_from_text(example_input: str):
    shapes, regions = day12.shapes_and_regions_from_text(example_input)

    assert len(shapes) == 6
    assert len(regions) == 3

    assert all(len(shape) == 7 for shape in shapes)
    assert all(len(region.shape_quantities) == 6 for region in regions)

    assert regions[0].dimensions == (4, 4)
    assert regions[1].dimensions == (12, 5)
    assert regions[2].dimensions == (12, 5)
