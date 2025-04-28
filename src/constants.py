import re
from collections import Counter
from typing import Dict, List


def filter_by_description(
        transactions: List[Dict], search_str: str) -> List[Dict]:
    """Фильтрует транзакции по строке в описании с использованием regex."""
    pattern = re.compile(search_str, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t["description"])]


def count_transactions_by_category(transactions: List[Dict]) -> Dict[str, int]:
    """Считает количество операций по категориям (описанию)."""
    return Counter(t["description"] for t in transactions)
