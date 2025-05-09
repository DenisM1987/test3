import pytest
import pandas as pd
from src.reports import (
    spending_by_category,
    spending_by_weekday,
    spending_by_workday
)


@pytest.fixture
def sample_transactions():
    return pd.DataFrame({
        'Дата операции': ['2023-01-01', '2023-01-02', '2023-02-01'],
        'Категория': ['Еда', 'Еда', 'Транспорт'],
        'Сумма операции': [100, 200, 300]
    })


def test_spending_by_category(sample_transactions):
    result = (spending_by_category
              (sample_transactions, 'Еда', '2023-02-01'))
    assert not result.empty
    assert result['Сумма операции'].sum() == 300


def test_spending_by_weekday(sample_transactions):
    result = spending_by_weekday(sample_transactions, '2023-02-01')
    assert not result.empty
    assert 'День недели' in result.columns


def test_spending_by_workday(sample_transactions):
    result = spending_by_workday(sample_transactions, '2023-02-01')
    assert not result.empty
    assert 'Тип дня' in result.columns
