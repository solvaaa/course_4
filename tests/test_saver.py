import pytest
from src.saver import JsonSaver
from src.description import Description


@pytest.fixture
def description_to_add():
    return Description(10000000, 'name1', 'https://1', {'from': 10000, 'to': 15000}, 'desc1')


def test_read_file():
    saver_read = JsonSaver(path='test_read.json')
    descriptions = saver_read.read_datafile()
    assert len(descriptions) == 20
    for desc in descriptions:
        assert isinstance(desc['id'], int)
        assert isinstance(desc['name'], str)
        assert isinstance(desc['salary'], dict)


def test_add_description(description_to_add):
    with open('test_read.json', 'r', encoding='utf-8') as file:
        raw_file = file.read()
    with open('test.json', 'w+', encoding='utf-8') as file:
        file.truncate(0)
        file.write(raw_file)
    saver = JsonSaver(path='test.json')
    saver.add_descriptions(description_to_add)
    new_descriptions = saver.read_datafile()
    assert len(new_descriptions) == 21


def test_delete_description(description_to_add):
    with open('test_read.json', 'r', encoding='utf-8') as file:
        raw_file = file.read()
    with open('test.json', 'w+', encoding='utf-8') as file:
        file.truncate(0)
        file.write(raw_file)
    saver = JsonSaver(path='test.json')
    saver.add_descriptions(description_to_add)
    saver.delete_description(description_to_add)
    new_descriptions = saver.read_datafile()
    assert len(new_descriptions) == 20


def test_get_by_keyword():
    saver = JsonSaver(path='test_read.json')
    filtered = saver.get_by_keyword('junior')
    assert len(filtered) == 7
