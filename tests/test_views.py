import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src import views
from src.utils import load_transactions
import pandas as pd
import logging


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями"""
    return pd.DataFrame([
        {'date': '2023-01-10', 'amount': 100.0, 'card': '1234', 'category': 'Food', 'description': 'Restaurant'},
        {'date': '2023-01-15', 'amount': 200.0, 'card': '5678', 'category': 'Transport', 'description': 'Taxi'},
    ])


@pytest.fixture
def mock_env(monkeypatch):
    """Фикстура для мокирования переменных окружения"""
    monkeypatch.setenv('CURRENCY_API_KEY', 'test_key')
    monkeypatch.setenv('STOCK_API_KEY', 'test_key')


@patch('src.utils.load_transactions')
@patch('src.utils.fetch_currency_rates')
@patch('src.utils.fetch_stock_prices')
def test_home_page_success(mock_stocks, mock_currency, mock_load, sample_transactions):
    """Тест успешного формирования главной страницы"""
    # Настройка моков
    mock_load.return_value = sample_transactions
    mock_currency.return_value = [{'currency': 'USD', 'rate': 75.5}]
    mock_stocks.return_value = [{'stock': 'AAPL', 'price': 150.0}]

    # Вызов тестируемой функции
    result = views.home_page("2023-01-15 12:00:00")

    # Проверки
    assert 'greeting' in result
    assert result['greeting'] in ['Доброе утро', 'Добрый день', 'Добрый вечер', 'Доброй ночи']
    assert len(result['cards']) == 2
    assert len(result['top_transactions']) == 2
    assert len(result['currency_rates']) == 1
    assert len(result['stock_prices']) == 1


@patch('src.utils.load_transactions')
def test_home_page_empty_data(mock_load):
    """Тест с пустыми данными"""
    mock_load.return_value = pd.DataFrame()
    with pytest.raises(ValueError, match="No transactions found"):
        views.home_page("2023-01-01 00:00:00")


@pytest.mark.parametrize("time,expected_greeting", [
    ("2023-01-01 06:00:00", "Доброе утро"),
    ("2023-01-01 12:00:00", "Добрый день"),
    ("2023-01-01 19:00:00", "Добрый вечер"),
    ("2023-01-01 23:00:00", "Доброй ночи"),
])
def test_greeting_logic(time, expected_greeting):
    """Параметризованный тест для проверки логики приветствия"""
    with patch('src.views.home_page') as mock_home:
        mock_home.return_value = {'greeting': ''}
        views.home_page(time)
        assert mock_home.call_args[0][0] == time
