import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def convert_currency_to_rub(transaction: Dict[str, Any]) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма транзакции в рублях (float) или None, если конвертация невозможна
    """
    if not transaction or 'amount' not in transaction or 'currency' not in transaction:
        return None

    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)

    if currency in ('USD', 'EUR'):
        try:
            response = requests.get(
                BASE_URL,
                params={'base': currency, 'symbols': 'RUB'},
                headers={'apikey': API_KEY},
                timeout=10
            )
            response.raise_for_status()

            rate = response.json()['rates']['RUB']
            return float(amount) * rate
        except (requests.RequestException, KeyError, ValueError):
            return None

    return None
