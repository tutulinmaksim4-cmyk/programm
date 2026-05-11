import pytest
from unittest.mock import patch, mock_open
from src.utils import get_transactions_data
import os

# 1. Тест на успешное чтение
@patch("os.path.exists", return_value=True)
@patch("builtins.open", mock_open(read_data='[{"id": 1}]'))
def test_get_transactions_data_success(mock_os_exists):
    # В аргументах только mock_os_exists, так как open подменен явно
    assert get_transactions_data("fake.json") == [{"id": 1}]


# 2. Тест на отсутствие файла
def test_get_transactions_data_not_found():
    with patch("os.path.exists", return_value=False):
        assert get_transactions_data("non_existent.json") == []


# 3. Тест на ошибки в данных
@pytest.mark.parametrize("bad_data", ["", 'invalid json', '{}'])
@patch("os.path.exists", return_value=True)
def test_get_transactions_data_errors(mock_os_exists, bad_data):
    # Сначала идет аргумент от @patch, потом от @parametrize
    with patch("builtins.open", mock_open(read_data=bad_data)):
        assert get_transactions_data("bad.json") == []
