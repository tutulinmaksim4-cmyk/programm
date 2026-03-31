from typing import Union
from src.masks import get_mask_account,get_mask_card_number

def mask_account_card (info: str) ->str:
    """Принимаем строку с типом и номером/счетом карты
    и возвращаем замаскированную версию"""
    #Разделяем строку по пробелам
    parts = info.split()
    #Последний элемент в списке НОМЕР
    number_str = parts[-1]
    #Элементы до последнего это название, склеиваем их обратно
    type_name = ''.join(parts[:-1])
    #Проверяем счет или карта
    if type_name.lower() == 'счет':
        # Если это счет, вызываем функцию для счета
        masked_number = get_mask_account(int(number_str))
    else:
        #Если это карта, вызываем функию для карты
        masked_number = get_mask_card_number(int(number_str))

        #Возвращаем готовую маскировку
        return f'{type_name} {masked_number}'

def get_date(data)
