"""
Основной модуль для запуска приложения
"""
from .views import home_page, events_page
from .services import profitable_cashback_categories
from .reports import spending_by_category

def main():
    """Пример использования функций"""
    # Пример вызова функции главной страницы
    home_data = home_page("2023-05-15 14:30:00")
    print(home_data)

if __name__ == "__main__":
    main()
