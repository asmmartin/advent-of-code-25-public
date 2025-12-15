import pytest

from advent_of_code_25 import day11


@pytest.fixture
def example_input() -> str:
    return (
        "aaa: you hhh\n"
        "you: bbb ccc\n"
        "bbb: ddd eee\n"
        "ccc: ddd eee fff\n"
        "ddd: ggg\n"
        "eee: out\n"
        "fff: out\n"
        "ggg: out\n"
        "hhh: ccc fff iii\n"
        "iii: out"
    )


@pytest.fixture
def example_input_2() -> str:
    return (
        "svr: aaa bbb\n"
        "aaa: fft\n"
        "fft: ccc\n"
        "bbb: tty\n"
        "tty: ccc\n"
        "ccc: ddd eee\n"
        "ddd: hub\n"
        "hub: fff\n"
        "eee: dac\n"
        "dac: fff\n"
        "fff: ggg hhh\n"
        "ggg: out\n"
        "hhh: out"
    )


def test_connections_from_text(example_input: str):
    connections = day11.Connections.from_text(example_input)

    assert len(connections.conns) == 11
    assert len(connections.conns["ddd"]) == 1
    assert len(connections.conns["you"]) == 2
    assert len(connections.conns["hhh"]) == 3


def test_connections_count_paths(example_input: str):
    connections = day11.Connections.from_text(example_input)
    path_count = connections.count_paths("you")

    assert path_count == 5


def test_good_path(example_input_2: str):
    connections = day11.Connections.from_text(example_input_2)

    svr_dac = connections.count_paths("svr", "dac")
    dac_fft = connections.count_paths("dac", "fft")
    fft_out = connections.count_paths("fft", "out")

    svr_fft = connections.count_paths("svr", "fft")
    fft_dac = connections.count_paths("fft", "dac")
    dac_out = connections.count_paths("dac", "out")

    result = (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out)

    assert result == 2
