import pytest
from unittest.mock import patch
from src.external_api import convert_currency_to_rub


@pytest.fixture
def rub_transaction():
    return {'amount': '100', 'currency': 'RUB'}


@pytest.fixture
def usd_transaction():
    return {'amount': '100', 'currency': 'USD'}


def test_convert_rub(rub_transaction):
    assert convert_currency_to_rub(rub_transaction) == 100.0


@patch('requests.get')
def test_convert_usd(mock_get, usd_transaction):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {'rates': {'RUB': 75.0}}

    result = convert_currency_to_rub(usd_transaction)
    assert result == 7500.0


def test_invalid_transaction():
    # Теперь ожидаем 0.0 вместо None
    assert convert_currency_to_rub({}) == 0.0
    assert convert_currency_to_rub({'amount': '100'}) == 0.0
    assert convert_currency_to_rub({'currency': 'USD'}) == 0.0


def test_invalid_amount():
    assert convert_currency_to_rub({'amount':
                                    'invalid', 'currency': 'USD'}) == 0.0


def test_unsupported_currency():
    assert convert_currency_to_rub({'amount': '100', 'currency': 'GBP'}) == 0.0
