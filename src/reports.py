"""
Функции для генерации отчетов:
- Траты по категории
- Траты по дням недели
- Траты в рабочие/выходные дни
"""
import pandas as pd
from typing import Optional


def report_decorator(filename=None):
    """Декоратор для сохранения отчетов в файл"""
    pass


@report_decorator
def spending_by_category(
        transactions: pd.DataFrame,
        category: str,
        date: Optional[str] = None) -> pd.DataFrame:
    """Отчет по тратам в категории за последние 3 месяца"""
    pass


@report_decorator('weekday_spending.json')
def spending_by_weekday(
        transactions: pd.DataFrame,
        date: Optional[str] = None) -> pd.DataFrame:
    """Отчет по тратам по дням недели"""
    pass
