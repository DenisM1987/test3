from . import utils_logger


def some_function(param: str) -> str:
    try:
        (utils_logger.debug
         (f"Вызвана функция some_function с параметром: {param}"))
        # Логика функции
        result = f"Processed {param}"
        (utils_logger.info
         (f"Функция some_function успешно выполнена. Результат: {result}"))
        return result
    except Exception as e:
        (utils_logger.error
         (f"Ошибка в функции some_function: {str(e)}", exc_info=True))
        raise
