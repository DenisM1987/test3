from typing import Dict, List

from transaction import (count_transactions_by_category,
                         filter_transactions_by_description)


def main() -> None:
    """Главная функция, взаимодействующая с пользователем."""
    print("Привет! "
          "Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    print(input("Ваш выбор: "))
    # Дальнейшая логика (загрузка файла, фильтрация, вывод)
