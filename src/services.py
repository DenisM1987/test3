"""
Сервисы анализа транзакций:
- Выгодные категории кешбэка
- Инвесткопилка
- Поиск транзакций
"""
from typing import List, Dict, Any


def profitable_cashback_categories(data: List[Dict[str, Any]],
                                   year: int, month: int) -> dict:
    """Анализ выгодных категорий для кешбэка"""
    pass


def investment_bank(month: str, transactions: List[Dict[str, Any]],
                    limit: int) -> float:
    """Расчет суммы для инвесткопилки"""
    pass


def simple_search(query: str, transactions: List[Dict[str, Any]]) \
        -> List[Dict[str, Any]]:
    """Простой поиск транзакций по запросу"""
    pass
