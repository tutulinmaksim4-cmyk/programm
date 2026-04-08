from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует список словарей по значению ключа state.
    Args:
    data: список словарей дял фильтрации
    state: статус по которому нужно отфильтровать значения
    Returns:
    Новый список словарей, соответствующий указанному статусу"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки по дате
    Args:
        data: список словарей для проверки
        reverse: Порядок сортировки

        Returns: новый отсортированный список"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
