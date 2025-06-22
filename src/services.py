def investment_bank(month: str, transactions: List[Dict], limit: int) -> float:
    """
    Рассчитывает сумму для инвесткопилки через округление трат.

    Args:
        month: Месяц в формате 'YYYY-MM'
        transactions: Список транзакций
        limit: Шаг округления (10, 50, 100)

    Returns:
        Сумма для инвесткопилки
    """
    if limit not in {10, 50, 100}:
        raise ValueError("Limit must be 10, 50 or 100")

    monthly_trans = [t for t in transactions if t['date'].startswith(month)]
    total = 0.0

    for trans in monthly_trans:
        amount = float(trans['amount'])
        if amount > 0:  # Только расходы
            rounded = math.ceil(amount / limit) * limit
            total += rounded - amount

    return round(total, 2)
