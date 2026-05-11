import pytest
from unittest.mock import patch, mock_open
from src.utils import get_transactions_data

def test_get_transactions_data_success():
    m_data = '[{"id": 1}]'
    with patch("builtins.open", mock_open(read_data=m_data)):
        assert get_transactions_data("fake.json") == [{"id": 1}]

def test_get_transactions_data_not_found():
    with patch("os.path.exists", return_value=False):
        assert get_transactions_data("non_existent.json") == []

@pytest.mark.parametrize("bad_data", ["", "invalid json", "{}"])
def test_get_transactions_data_errors(bad_data):
    with patch("builtins.open", mock_open(read_data=bad_data)):
        assert get_transactions_data("bad.json") == []