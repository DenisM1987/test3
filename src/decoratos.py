import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, логирующий работу функции (в файл или консоль)."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Запись логов
            try:
                result = func(*args, **kwargs)
                log_message = (f"{func.__name__} ok at "
                               f"{datetime.datetime.now()}\n")
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                return result
            except Exception as e:
                error_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")
                raise e

        return wrapper

    return decorator
