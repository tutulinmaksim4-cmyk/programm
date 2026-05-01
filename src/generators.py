def filter_by_currency(transactions, currency_code):
    """
    Принимает список транзакций и код валюты (например, 'USD').
    Возвращает итератор с транзакциями, где код валюты совпадает с заданным.
    """
    for transaction in transactions:
    # Проверяем наличие вложенных ключей, чтобы избежать ошибок

        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
       Принимает список транзакций и поочередно
       выдает значение ключа 'description'.
    """
    for transaction in transactions:
    # Достаем описание. Если ключа вдруг нет, вернем пустую строку или текст об ошибке.
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, stop):
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX в диапазоне от start до stop.
    """
    # Мы идем циклом от начального до конечного числа (включительно)
    for number in range(start, stop + 1):
        #Превращаем число в строку и добавляем нули в начало, чтобы всего было 16 цифр
        #{number:016} :016 означает "сделай строку длиной 16, если символов меньше - заполни нулями"
        card_str = f"{number:016}"

        formatted_card = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        #Отдаем готовый номер наружу
        yield formatted_card
