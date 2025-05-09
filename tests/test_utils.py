import pytest
from src.utils import (
    get_greeting,
    calculate_cashback,
    filter_transactions_by_date,
    group_transactions_by_category
)


@pytest.mark.parametrize("time,expected", [
    ('06:00:00', 'Доброе утро'),
    ('12:00:00', 'Добрый день'),
    ('18:00:00', 'Добрый вечер'),
    ('23:00:00', 'Доброй ночи'),
])
def test_get_greeting(time, expected):
    assert get_greeting(f'2023-01-01 {time}') == expected


def test_calculate_cashback():
    assert calculate_cashback(1000) == 10
    assert calculate_cashback(150) == 1.5


def test_filter_transactions_by_date(sample_transactions):
    filtered = filter_transactions_by_date(
        sample_transactions,
        '2023-01-01',
        '2023-01-31'
    )
    assert len(filtered) == 2


def test_group_transactions_by_category(sample_transactions):
    grouped = group_transactions_by_category(sample_transactions)
    assert 'Супермаркеты' in grouped
    assert grouped['Супермаркеты'] == 100
