import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected


def test_get_date():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
    assert get_date("2024-12-31T23:59:59") == "31.12.2024"


def test_get_data():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
    assert get_date("2024-12-31T23:59:59.000000") == "31.12.2024"
