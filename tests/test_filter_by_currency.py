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

@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),  # Валюта есть в списке (2 шт)
    ("RUB", 1),  # Валюта есть в списке (1 шт)
    ("EUR", 0),  # Валюты нет в списке
    ("", 0)      # Пустой запрос
])
def test_filter_by_currency_parameterized(transactions_list, currency, expected_count):
    """Параметризованный тест фильтрации валют"""
    result = list(filter_by_currency(transactions_list, currency))
    assert len(result) == expected_count
    for trans in result:
        assert trans["operationAmount"]["currency"]["code"] == currency

def test_filter_by_currency_empty_input():
    """Отдельный тест на пустой входной список (не требует параметризации)"""
    assert list(filter_by_currency([], "USD")) == []

# --- ТЕСТЫ transaction_descriptions ---

@pytest.mark.parametrize("index, expected_description", [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Перевод с карты на карту")
])
def test_transaction_descriptions_values(transactions_list, index, expected_description):
    """Проверка конкретных описаний по индексам через параметризацию"""
    descriptions = list(transaction_descriptions(transactions_list))
    assert descriptions[index] == expected_description

def test_transaction_descriptions_correct(transactions_list):
    """Проверка возвращаемых описаний"""
    descriptions = transaction_descriptions(transactions_list)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


# --- ТЕСТЫ card_number_generator ---

@pytest.mark.parametrize("start, stop, expected_first, expected_last, expected_len", [
    (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003", 3),
    (10, 10, "0000 0000 0000 0010", "0000 0000 0000 0010", 1),
    (9999999999999998, 9999999999999999, "9999 9999 9999 9998", "9999 9999 9999 9999", 2)
])
def test_card_number_generator_params(start, stop, expected_first, expected_last, expected_len):
    """Проверка генератора карт с разными диапазонами"""
    result = list(card_number_generator(start, stop))
    assert len(result) == expected_len
    assert result[0] == expected_first
    assert result[-1] == expected_last

@pytest.mark.parametrize("number", [1, 100, 9999])
def test_card_number_generator_format(number):
    """Проверка правильности формата (пробелы и длина) для разных чисел"""
    gen = card_number_generator(number, number)
    card = next(gen)
    # Проверка формата XXXX XXXX XXXX XXXX (19 символов с пробелами)
    assert len(card) == 19
    assert card[4] == " "
    assert card[9] == " "
    assert card[14] == " "
    # Проверяем, что внутри нет букв, только цифры и пробелы
    assert card.replace(" ", "").isdigit()

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