import pytest
from src import services
from datetime import datetime
from typing import List, Dict

@pytest.fixture
def transactions_data() -> List[Dict]:
    """Фикстура с тестовыми транзакциями для сервисов"""
    return [
        {'date': '2023-01-05', 'amount': '1712.00', 'category': 'Food'},
        {'date': '2023-01-10', 'amount': '325.50', 'category': 'Transport'},
        {'date': '2023-01-15', 'amount': '1200.00', 'category': 'Shopping'},
    ]

@pytest.mark.parametrize("month,limit,expected", [
    ('2023-01', 10, 8.5),
    ('2023-01', 50, 28.0),
    ('2023-01', 100, 78.0),
])
def test_investment_bank(transactions_data, month, limit, expected):
    """Параметризованный тест для инвесткопилки"""
    result = services.investment_bank(month, transactions_data, limit)
    assert result == expected

def test_investment_bank_invalid_limit(transactions_data):
    """Тест на невалидный лимит"""
    with pytest.raises(ValueError, match="Limit must be 10, 50 or 100"):
        services.investment_bank('2023-01', transactions_data, 25)

def test_profitable_cashback_categories(transactions_data):
    """Тест для выгодных категорий кешбэка"""
    result = services.profitable_cashback_categories(transactions_data, 2023, 1)
    assert isinstance(result, dict)
    assert 'Food' in result
    assert result['Food'] == pytest.approx(17.12, 0.01)

@patch('src.services.re.findall')
def test_phone_number_search(mock_find, transactions_data):
    """Тест поиска по телефонным номерам"""
    mock_find.return_value = ['+7 999 123-45-67']
    transactions_data[0]['description'] = 'Payment +7 999 123-45-67'
    result = services.find_phone_transactions(transactions_data)
    assert len(result) == 1
    assert '+7 999 123-45-67' in result[0]['description']
