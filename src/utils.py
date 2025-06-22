def get_greeting(date_time: str) -> str:
    """Возвращает приветствие в зависимости от времени суток"""
    pass

def get_transactions_from_excel() -> pd.DataFrame:
    """Загружает транзакции из Excel-файла"""
    pass

def filter_transactions_by_date(transactions: pd.DataFrame, date_time: str) -> pd.DataFrame:
    """Фильтрует транзакции по дате"""
    pass

def get_cards_info(transactions: pd.DataFrame) -> list:
    """Возвращает информацию по картам"""
    pass

def get_top_transactions(transactions: pd.DataFrame, limit: int) -> list:
    """Возвращает топ транзакций по сумме"""
    pass

def get_currency_rates() -> list:
    """Получает курсы валют из API"""
    pass

def get_stock_prices() -> list:
    """Получает цены акций из API"""
    pass
