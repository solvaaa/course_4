import pytest
from src.description import Description


@pytest.fixture
def description1():
    return Description(12345678, 'name1', 'https://1', {'from': 10000, 'to': 15000}, 'desc1', '2023-07-06 18:52:14')


@pytest.fixture
def description2():
    return Description(12345888, 'name2', 'https://2', {'from': 12000, 'to': 20000}, 'desc2', '2023-06-30 13:21:39')


@pytest.fixture
def description3():
    return Description(12345998, 'name3', 'https://3', {'from': None, 'to': 20000}, 'desc2', '2023-07-09 18:45:53')


def test_str(description1):
    assert str(description1) == 'name1'


def test_comparison(description1, description2):
    assert not(description1 == description2)
    assert description1 != description2
    assert description1 < description2
    assert description1 <= description2
    assert not(description1 > description2)
    assert not(description1 >= description2)


def test_filter_with_salary(description1, description2, description3):
    descriptions = [description1, description2, description3]
    filtered = Description.filter_with_salary(descriptions)
    assert len(filtered) == 2
    for desc in filtered:
        assert isinstance(desc.salary['from'], int)


def test_sort_by_salary(description1, description2, description3):
    descriptions = [description1, description2, description3]
    sorted = Description.sort_by_salary(descriptions)
    assert len(sorted) == 3
    for i in range(2):
        assert sorted[i] >= sorted[i + 1]


def test_sort_by_date(description1, description2, description3):
    descriptions = [description1, description2, description3]
    sorted = Description.sort_by_date(descriptions)
    assert len(sorted) == 3
    for i in range(2):
        assert sorted[i].date_published >= sorted[i + 1].date_published
