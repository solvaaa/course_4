import pytest
from src.api import HeadHunter, SuperJob

@pytest.fixture
def hh():
    return HeadHunter(per_page=20)


@pytest.fixture
def sj():
    return SuperJob(per_page=20)


def test_headhunter_get_info(hh):
    info = hh.get_info('python')
    assert isinstance(info, list)
    assert len(info)
    for item in info:
        assert len(item['id']) == 8
        assert isinstance(item['name'], str)


def test_headhunter_output_info(hh):
    info = hh.output_info('python')
    assert isinstance(info, list)
    assert len(info)
    for item in info:
        assert isinstance(item['id'], int)
        assert isinstance(item['name'], str)
        salary_type = item['salary']['from']
        assert salary_type is None or isinstance(salary_type, int)


def test_superjob_get_info(sj):
    info = sj.get_info('python')
    assert isinstance(info, list)
    assert len(info)
    for item in info:
        assert isinstance(item['id'], int)
        assert isinstance(item['profession'], str)


def test_superjob_output_info(sj):
    info = sj.output_info('python')
    assert isinstance(info, list)
    assert len(info)
    for item in info:
        assert isinstance(item['id'], int)
        assert isinstance(item['name'], str)
        salary_type = item['salary']['from']
        assert salary_type is None or isinstance(salary_type, int)