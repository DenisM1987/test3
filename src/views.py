"""
Функции для генерации JSON ответов для веб-страниц:
- Главная страница
- Страница событий
"""
from .utils import load_transactions, filter_transactions_by_date


def home_page(date_time: str) -> dict:
    """
    Генерация данных для главной страницы
    Args:
        date_time: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'
    Returns:
        dict: JSON-ответ для главной страницы
    """
    transactions = load_transactions()  # Пример использования импортированной функции
    filtered_transactions = filter_transactions_by_date(transactions, date_time)
    return {"data": filtered_transactions}


def events_page(date_time: str, period: str = 'M') -> dict:
    """
    Генерация данных для страницы событий
    Args:
        date_time: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'
        period: Период ('W', 'M', 'Y', 'ALL')
    Returns:
        dict: JSON-ответ для страницы событий
    """
    transactions = load_transactions()
    filtered_transactions = filter_transactions_by_date(transactions, date_time)
    return {"events": filtered_transactions, "period": period}
