def home_page(date_time: str) -> dict:
    """
    Генерирует JSON-данные для главной страницы.
    
    Args:
        date_time: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'
    
    Returns:
        Словарь с данными для главной страницы
    """
    # Получение данных из Excel
    transactions = utils.get_transactions_from_excel()
    
    # Фильтрация данных по дате
    filtered_data = utils.filter_transactions_by_date(transactions, date_time)
    
    # Формирование ответа
    response = {
        "greeting": utils.get_greeting(date_time),
        "cards": utils.get_cards_info(filtered_data),
        "top_transactions": utils.get_top_transactions(filtered_data, 5),
        "currency_rates": utils.get_currency_rates(),
        "stock_prices": utils.get_stock_prices()
    }

    except Exception as e:
    logging.error(f"Error in home_page: {str(e)}")
    raise
