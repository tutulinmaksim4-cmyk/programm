import json
import os
import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

# Логер для модуля utils
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

# Файл utils.log в папке logs
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Пример:
# logger.info("Чтение данных из JSON-файла начато")

import json


def get_data(path: str) -> list:
    logger.info(f"Попытка загрузки данных из файла: {path}")
    """Читает данные о транзакциях из JSON-файла."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # ЛОГ: Успешное завершение
            logger.info("Данные успешно загружены")
            return data

    except FileNotFoundError:
        # ЛОГ: Ошибка (файл не найден)
        logger.error(f"Файл не найден по пути: {path}")
        return []

    except json.JSONDecodeError:
        # ЛОГ: Ошибка (битый JSON)
        logger.error(f"Ошибка декодирования JSON в файле: {path}")
        return []

