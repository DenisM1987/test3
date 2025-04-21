import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def convert_currency_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    В случае ошибки возвращает 0.0.

    Args:
        transaction: Словарь с данными о транзакции,
        включая 'amount' и 'currency'.

    Returns:
        Сумма транзакции в рублях (float). При ошибках — 0.0.
    """
    default_fallback = 0.0  # Значение по умолчанию при ошибках

    if (not transaction or 'amount' not in transaction
            or 'currency' not in transaction):
        logger.error("Неверный формат транзакции: "
                     "отсутствует 'amount' или 'currency'")
        return default_fallback

    try:
        amount = float(transaction['amount'])
    except (TypeError, ValueError):
        logger.error(f"Невозможно преобразовать amount:"
                     f" {transaction['amount']}")
        return default_fallback

    currency = transaction['currency'].upper()

    if currency == 'RUB':
        return amount

    if currency in ('USD', 'EUR'):
        try:
            response = requests.get(
                BASE_URL,
                params={'base': currency, 'symbols': 'RUB'},
                headers={'apikey': API_KEY},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            rate = data['rates']['RUB']
            return amount * rate
        except requests.RequestException as e:
            logger.error(f"Ошибка запроса к API: {e}")
        except (KeyError, ValueError) as e:
            logger.error(f"Ошибка обработки ответа API: {e}")
        return default_fallback

    logger.error(f"Неподдерживаемая валюта: {currency}")
    return default_fallback
