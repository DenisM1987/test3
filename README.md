# homework_11_2 #

## Декоратор `log` ##

Логирует вызовы функций:
- Время выполнения.
- Аргументы.
- Результат или ошибку.

### Использование ###
```python
from src.decorators import log

@log(filename="app.log")
def my_func(x, y):
    return x / y

