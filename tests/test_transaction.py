import pytest

from src.transaction import (count_transactions_by_category,
                             filter_transactions_by_description)


def test_filter_transactions_by_description():
    transactions = [
        {"description": "Перевод организации", "status": "EXECUTED"},
        {"description": "Открытие вклада", "status": "EXECUTED"},
    ]
    result = filter_transactions_by_description(transactions, "перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"


def test_count_transactions_by_category():
    transactions = [
        {"description": "Перевод", "status": "EXECUTED"},
        {"description": "Перевод", "status": "CANCELED"},
        {"description": "Покупка", "status": "EXECUTED"},
    ]
    categories = ["перевод", "покупка"]
    result = count_transactions_by_category(transactions, categories)
    assert result == {"перевод": 2, "покупка": 1}
