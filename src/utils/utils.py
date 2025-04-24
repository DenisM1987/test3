import logging
from typing import Any

# Создаем логер для модуля utils
logger = logging.getLogger('utils')


def setup_logging() -> None:
    """Настройка логирования для модуля utils"""
    logger.setLevel(logging.DEBUG)

    # Создаем файловый обработчик
    file_handler = logging.FileHandler('logs/utils.log', mode='w')
    file_handler.setLevel(logging.DEBUG)

    # Создаем форматтер
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Настраиваем обработчик
    file_handler.setFormatter(file_formatter)

    # Добавляем обработчик к логеру
    logger.addHandler(file_handler)


def example_function(value: Any) -> Any:
    """Пример функции с логированием"""
    try:
        (logger.debug
         (f"Вызов example_function с аргументом: {value}"))
        result = value * 2
        (logger.info
         (f"Функция example_function успешно выполнена. Результат: {result}"))
        return result
    except Exception as e:
        (logger.error
         (f"Ошибка в example_function: {str(e)}", exc_info=True))
        raise


# Инициализация логирования при импорте модуля
setup_logging()
