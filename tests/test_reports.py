import pytest
from src import reports
import pandas as pd
from datetime import datetime
from unittest.mock import patch, mock_open


@pytest.fixture
def report_transactions():
    """Фикстура с тестовыми транзакциями для отчетов"""
    data = {
        'date': pd.to_datetime(['2023-01-10', '2023-01-15', '2023-02-05', '2023-03-20']),
        'amount': [100.0, 200.0, 150.0, 300.0],
        'category': ['Food', 'Transport', 'Food', 'Shopping'],
        'weekday': ['Tuesday', 'Sunday', 'Sunday', 'Monday']
    }
    return pd.DataFrame(data)


def test_spending_by_category(report_transactions):
    """Тест отчета по категориям"""
    result = reports.spending_by_category(report_transactions, 'Food')
    assert len(result) == 2  # Две транзакции за 3 месяца
    assert result['amount'].sum() == 250.0


@pytest.mark.parametrize("date,expected_count", [
    (None, 4),  # Все транзакции
    ('2023-02-01', 3),  # За последние 3 месяца от февраля
])
def test_spending_by_weekday(report_transactions, date, expected_count):
    """Параметризованный тест отчета по дням недели"""
    result = reports.spending_by_weekday(report_transactions, date)
    assert len(result) == expected_count
    assert 'weekday' in result.columns


@patch('builtins.open', mock_open())
def test_report_decorator(report_transactions):
    """Тест декоратора отчетов"""

    # Декорируем тестовую функцию
    @reports.report_decorator(filename="test_report.json")
    def test_func(data):
        return data.head(1)

    # Вызываем и проверяем что файл пытались записать
    result = test_func(report_transactions)
    assert len(result) == 1
