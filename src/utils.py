import json
import os


def get_transactions_data(path):
    """Читает данные о транзакциях из JSON-файла."""
    # Если путь не существует
    if not os.path.exists(path):
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Проверяем, что внутри список
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        # Если файл пустой или битый JSON

        return []
