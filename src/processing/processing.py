from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    return sorted(data, key=lambda x: x["date"], reverse=reverse)


if __name__ == "__main__":
    test_data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
    ]
    print("Фильтрация (EXECUTED):", filter_by_state(test_data))
    print("Сортировка:", sort_by_date(test_data))
