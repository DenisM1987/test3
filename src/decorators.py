import datetime
import sys
from typing import Any, Callable, Optional, TextIO


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Если указан, логи пишутся в файл, иначе — в консоль.

    Returns:
        Декорированная функция с логированием.
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Формируем сообщение
            func_name = func.__name__
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result = func(*args, **kwargs)
                msg = f"{timestamp} {func_name} ok\n"
            except Exception as e:
                msg = f"{timestamp} {func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(msg)
                else:
                    sys.stderr.write(msg)
                raise e

            # Записываем лог
            if filename:
                with open(filename, "a") as f:
                    f.write(msg)
            else:
                print(msg, end="")

            return result

        return wrapper

    return decorator
