import pytest
from src.services import (
    profitable_cashback_categories,
    investment_bank,
    simple_search,
    find_phone_transactions,
    find_person_transfers
)


@pytest.fixture
def sample_transactions():
    return [
        {'Дата операции': '2023-01-01', 'Категория':
            'Супермаркеты', 'Сумма операции': 1000, 'Кешбэк': 10},
        {'Дата операции': '2023-01-02', 'Категория':
            'Транспорт', 'Сумма операции': 500, 'Кешбэк': 5},
    ]


def test_profitable_cashback_categories(sample_transactions):
    result = profitable_cashback_categories(sample_transactions, 2023, 1)
    assert 'Супермаркеты' in result
    assert result['Супермаркеты'] == 10


def test_investment_bank(sample_transactions):
    result = investment_bank('2023-01', sample_transactions, 100)
    assert isinstance(result, float)


def test_simple_search(sample_transactions):
    result = simple_search('Супермаркеты', sample_transactions)
    assert len(result) == 1


def test_find_phone_transactions():
    transactions = [{'Описание': 'Пополнение +7 999 123-45-67'}]
    result = find_phone_transactions(transactions)
    assert len(result) == 1


def test_find_person_transfers():
    transactions = [{'Категория': 'Переводы', 'Описание': 'Иван С.'}]
    result = find_person_transfers(transactions)
    assert len(result) == 1
