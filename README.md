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
