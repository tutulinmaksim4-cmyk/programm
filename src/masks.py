import logging
import os

# 1. Создаем папку logs, если её еще нет
if not os.path.exists('logs'):
    os.makedirs('logs')

# 2. Создаем логер для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# 3. Настраиваем запись в файл masks.log в папке logs
# mode='w' — чтобы файл перезаписывался при каждом запуске
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')

# 4. Задаем формат: время - имя модуля - уровень - сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 5. Добавляем обработчик к логеру
logger.addHandler(file_handler)

# Пример использования (добавь в свои функции):
# logger.info("Маскировка номера карты выполнена успешно")
# logger.error("Ошибка при маскировке номера счета")

def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер банковской карты"""
    card_str = str(card_number)

    logger.info(f"Начата маскировка карты: {card_str}")

    if not card_str.isdigit() or len(card_str) != 16:
        logger.error(f"Некорректный формат номера карты: {card_str}")
        return ""

    # 3. Делаем маску
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: int) -> str:
    """Функция которая принимает на вход номер счета и возвращает его в маску формате"""
    acc_str = str(account_number)

    logger.info(f"Начата маскировка счета: {acc_str}")

    if not acc_str.isdigit():
        logger.error(f"Номер счета содержит не только цифры: {acc_str}")
        return ""

    return f"**{acc_str[-4:]}"

