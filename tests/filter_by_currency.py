import pytest
# Замените 'src.generators' на имя вашего модуля, где лежат функции
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator



@pytest.fixture
def transactions_list():
    """Фикстура со стандартным списком транзакций"""
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"currency": {"code": "USD"}}
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"currency": {"code": "RUB"}}
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"currency": {"code": "USD"}}
        }
    ]

@pytest.fixture
def empty_list():
    """Фикстура для пустого списка"""
    return []


# --- ТЕСТЫ filter_by_currency ---

def test_filter_by_currency_usd(transactions_list):
    """Проверка фильтрации существующей валюты (USD)"""
    result = list(filter_by_currency(transactions_list, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3

def test_filter_by_currency_not_found(transactions_list):
    """Проверка случая, когда такой валюты нет в списке"""
    result = list(filter_by_currency(transactions_list, "EUR"))
    assert len(result) == 0

# --- ТЕСТЫ transaction_descriptions ---

def test_transaction_descriptions_correct(transactions_list):
    """Проверка возвращаемых описаний"""
    descriptions = transaction_descriptions(transactions_list)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


# --- ТЕСТЫ card_number_generator ---

def test_card_number_generator_values():
    """Проверка значений и диапазона"""
    # Здесь фикстура не нужна, так как мы тестируем генерацию чисел
    cards = list(card_number_generator(1, 2))
    assert cards[0] == "0000 0000 0000 0001"
    assert cards[1] == "0000 0000 0000 0002"
    assert len(cards) == 2


def test_card_number_generator_large_numbers():
    """Проверка работы с большими числами (границы)"""
    start = 9999999999999998
    stop = 9999999999999999
    cards = list(card_number_generator(start, stop))
    assert cards[1] == "9999 9999 9999 9999"