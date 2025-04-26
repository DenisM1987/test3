from typing import Dict, List

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict]:
    """
    Читает финансовые операции из CSV-файла и возвращает список словарей.

    Args:
        file_path (str): Путь к CSV-файлу

    Returns:
        List[Dict]: Список словарей с транзакциями
    """
    try:
        data = pd.read_csv(file_path)
        return data.to_dict('records')
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return []


def read_excel_file(file_path: str) -> List[Dict]:
    """
    Читает финансовые операции из Excel-файла и возвращает список словарей.

    Args:
        file_path (str): Путь к Excel-файлу

    Returns:
        List[Dict]: Список словарей с транзакциями
    """
    try:
        data = pd.read_excel(file_path)
        return data.to_dict('records')
    except Exception as e:
        print(f"Ошибка при чтении Excel файла: {e}")
        return []
