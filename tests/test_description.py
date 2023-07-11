import pytest
from src.description import Description


@pytest.fixture
def description1():
    return Description(12345678, 'name1', 'https://1', {'from': 10000, 'to': 15000}, 'desc1')


@pytest.fixture
def description2():
    return Description(12345888, 'name2', 'https://2', {'from': 12000, 'to': 20000}, 'desc2')


def test_str(description1):
    assert str(description1) == 'name1'


def test_comparison(description1, description2):
    assert not(description1 == description2)
    assert description1 != description2
    assert description1 < description2
    assert description1 <= description2
    assert not(description1 > description2)
    assert not(description1 >= description2)

