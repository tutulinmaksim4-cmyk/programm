import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_to_rub_usd(mock_get):
    # Имитируем ответ от API
    mock_get.return_value.json.return_value = {"result": 7500.0}
    mock_get.return_value.status_code = 200

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }
    assert convert_to_rub(transaction) == 7500.0


def test_convert_to_rub_local():
    transaction = {
        "operationAmount": {"amount": "500", "currency": {"code": "RUB"}}
    }
    # Здесь Mock не нужен, так как запроса к API не будет

    assert convert_to_rub(transaction) == 500.0
