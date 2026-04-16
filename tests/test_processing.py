import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512359"},
        {"id": 93979522, "state": "CANCELED", "date": "2018-06-16T13:46:13.068128"},
        {"id": 59422340, "state": "EXECUTED", "date": "2020-01-01T12:00:00.000000"},
    ]


def test_filter_by_state(sample_data):
    # Тест фильтрации EXECUTED
    result = filter_by_state(sample_data, "EXECUTED")
    assert len(result) == 2
    assert result[0]["id"] == 41428829

    # Тест фильтрации CANCELED
    result_canceled = filter_by_state(sample_data, "CANCELED")
    assert len(result_canceled) == 1


def test_sort_by_date(sample_data):
    # По умолчанию (reverse=True) — сначала новые
    result = sort_by_date(sample_data)
    assert result[0]["id"] == 59422340  # 2020 год

    # По возрастанию (reverse=False) — сначала старые
    result_asc = sort_by_date(sample_data, reverse=False)
    assert result_asc[0]["id"] == 93979522  # 2018 год
