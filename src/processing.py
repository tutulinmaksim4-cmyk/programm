from typing import Any, Dict, List

def filter_by_state (data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует список словарей по значению ключа state"""

    return [item for item in data if item.get("state") == state]



def sort_by_date (data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция сортировки по дате"""

    return sorted(data, key=lambda x:x["data"], reverse=reverse)
