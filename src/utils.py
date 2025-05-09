# Импорт json
# from typing import Any, Dict, List


# def read_json_file(file_path: str) -> List[Dict[str, Any]]:
#     """
#     Читает JSON-файл и возвращает список словарей с данными о транзакциях.
#
#     Args:
#         file_path: Путь к JSON-файлу
#
#     Returns:
#         Список словарей с данными о транзакциях. Если файл пустой,
#         содержит не список или не найден, возвращается пустой список.
#     """
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#
#             if isinstance(data, list):
#                 return data
#             return []
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

"""
Вспомогательные функции для работы с транзакциями:
- Загрузка данных из Excel
- Фильтрация транзакций по дате
- Расчет статистик (суммы, кешбэка и т.д.)
- Форматирование данных для ответов
"""
import pandas as pd


def load_transactions(filepath: str) -> pd.DataFrame:
    """Загрузка транзакций из Excel файла"""
    pass


def filter_transactions_by_date(
        df: pd.DataFrame, start_date:
        str, end_date: str
        ) -> pd.DataFrame:
    """Фильтрация транзакций по диапазону дат"""
    pass


def calculate_cashback(amount: float) -> float:
    """Расчет кешбэка (1% от суммы)"""
    pass
