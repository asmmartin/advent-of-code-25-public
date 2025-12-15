import pytest

from advent_of_code_25 import day08


@pytest.fixture
def example_input() -> str:
    return (
        "162,817,812\n"
        "57,618,57\n"
        "906,360,560\n"
        "592,479,940\n"
        "352,342,300\n"
        "466,668,158\n"
        "542,29,236\n"
        "431,825,988\n"
        "739,650,466\n"
        "52,470,668\n"
        "216,146,977\n"
        "819,987,18\n"
        "117,168,530\n"
        "805,96,715\n"
        "346,949,466\n"
        "970,615,88\n"
        "941,993,340\n"
        "862,61,35\n"
        "984,92,344\n"
        "425,690,689"
    )


def test_read_coords(example_input: str):
    coords = day08.read_coords(example_input)

    assert len(coords) == 20
    assert all(len(c) == 3 for c in coords)


def test_count_close_circuit_junctions(example_input: str):
    coords = day08.read_coords(example_input)
    close_circuits_junctions_count = day08.count_close_circuit_junctions(coords, 10)

    assert close_circuits_junctions_count == [5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1]


def test_connect_all_boxes(example_input: str):
    coords = day08.read_coords(example_input)
    connections = day08.connect_all_boxes(coords)

    connections.sort()

    assert connections[-1][1][0][0] * connections[-1][1][1][0] == 25272


def test_connect_all_boxes_prims(example_input: str):
    coords = day08.read_coords(example_input)
    connections = day08.connect_all_boxes_prims(coords)

    connections.sort()

    assert connections[-1][1][0][0] * connections[-1][1][1][0] == 25272


def test_connect_all_boxes_kruskals(example_input: str):
    coords = day08.read_coords(example_input)
    connections = day08.connect_all_boxes_kruskals(coords)

    connections.sort()

    assert connections[-1][1][0][0] * connections[-1][1][1][0] == 25272
