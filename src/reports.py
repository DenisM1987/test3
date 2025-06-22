@report_decorator(filename="category_spending.json")
def spending_by_category(
        transactions: pd.DataFrame,
        category: str,
        date: Optional[str] = None
) -> pd.DataFrame:
    """
    Анализирует траты по категории за последние 3 месяца

    Args:
        transactions: DataFrame с транзакциями
        category: Название категории
        date: Дата отсчета (по умолчанию текущая)

    Returns:
        DataFrame с результатами анализа
    """
    date = pd.to_datetime(date) if date else pd.Timestamp.now()
    start_date = date - pd.DateOffset(months=3)

    filtered = transactions[
        (transactions['category'] == category) &
        (transactions['date'] >= start_date) &
        (transactions['date'] <= date)
        ]

    return filtered.groupby(pd.Grouper(key='date', freq='M'))['amount'].sum().reset_index()
