## Декоратор `log`

### Функционал
- Логирует вызовы функций.
- Поддерживает вывод в файл или консоль.
- Фиксирует ошибки с аргументами.

### Использование

from src.decorators import log

@log(filename="app.log")
def multiply(a: int, b: int) -> int:
    return a * b


### Пример логов

multiply ok at 2024-05-20 14:30:00
multiply error: ValueError. Inputs: (1, "a"), {}

## Новая функциональность

Добавлена поддержка чтения финансовых операций из:
- CSV файлов (функция `read_csv_file()`)
- Excel файлов (функция `read_excel_file()`)

Пример использования:
```python
from src.file_operations import read_csv_file, read_excel_file

csv_transactions = read_csv_file('data/transactions.csv')
excel_transactions = read_excel_file('data/transactions_excel.xlsx')
