import re
from collections import Counter
from typing import Dict, List


def filter_transactions_by_description(
        transactions: List[Dict], search_str: str) -> List[Dict]:
    """
    Фильтрует транзакции по строке в описании.

    Args:
        transactions: Список словарей с транзакциями.
        search_str: Строка для поиска в описании.

    Returns:
        Список транзакций, где description содержит search_str.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [t for t in transactions
            if pattern.search(t.get("description", ""))]


def count_transactions_by_category(
        transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям.

    Args:
        transactions: Список транзакций.
        categories: Список категорий для подсчета.

    Returns:
        Словарь {категория: количество}.
    """
    descriptions = [t.get("description", "").lower() for t in transactions]
    return Counter(desc for desc in descriptions if desc in categories)
