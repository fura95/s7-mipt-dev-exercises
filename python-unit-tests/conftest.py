import pytest


@pytest.fixture()
def example_fixture():
    print('Hello, we start testing')
    yield
    print("Goodbye")