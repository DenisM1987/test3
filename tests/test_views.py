import pytest
import pandas as pd
from unittest.mock import patch  # Добавьте этот импорт
from src.views import home_page, events_page


@pytest.fixture
def sample_transactions():
    return pd.DataFrame({
        'Дата операции': ['2023-01-01', '2023-01-02'],
        'Номер карты': ['1234', '5678'],
        'Сумма платежа': [100, 200],
        'Категория': ['Супермаркеты', 'Транспорт'],
        'Описание': ['Покупка', 'Такси'],
        'Кешбэк': [1, 2]
    })


@patch('src.views.get_currency_rates')
@patch('src.views.get_stock_prices')
@patch('src.views.load_transactions')
def test_home_page(mock_load, mock_stocks,
                   mock_currency, sample_transactions):
    mock_load.return_value = sample_transactions
    mock_stocks.return_value = [{'stock': 'AAPL', 'price': 150}]
    mock_currency.return_value = [{'currency': 'USD', 'rate': 75}]
    result = home_page('2023-01-02 12:00:00')

    assert 'greeting' in result
    assert 'cards' in result
    assert len(result['cards']) == 2
    assert 'top_transactions' in result


@patch('src.views.get_currency_rates')
@patch('src.views.get_stock_prices')
@patch('src.views.load_transactions')
def test_events_page(mock_load, mock_stocks,
                     mock_currency, sample_transactions):
    mock_load.return_value = sample_transactions
    mock_stocks.return_value = [{'stock': 'AAPL', 'price': 150}]
    mock_currency.return_value = [{'currency': 'USD', 'rate': 75}]
    result = events_page('2023-01-02')

    assert 'expenses' in result
    assert 'income' in result
    assert result['expenses']['total_amount'] == 300
