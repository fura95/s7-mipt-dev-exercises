import pytest
import math

from main import logarithm


@pytest.fixture()
def numbers():
    return [1, 2, 4, 8, 16, 32]


def test_example(example_fixture, numbers):
    for i in numbers:
        x = math.e ** i
        y = logarithm(x)
        print(y)
        assert y == i
