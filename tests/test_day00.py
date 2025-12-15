import pytest


@pytest.fixture
def example_input() -> str:
    return (
        "Example Line 1\nExample Line 2\nExample Line 3\nExample Line 4\nExample Line 5"
    )
