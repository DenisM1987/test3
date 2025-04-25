import logging
from typing import Optional, Union

# Создаем логер для модуля masks
logger = logging.getLogger('masks')


def setup_logging() -> None:
    """Настройка логирования для модуля masks"""
    logger.setLevel(logging.DEBUG)

    # Создаем файловый обработчик
    file_handler = logging.FileHandler('logs/masks.log', mode='w')
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


def mask_card_number(card_number: Union[str, int]) -> Optional[str]:
    """Маскирует номер карты"""
    try:
        (logger.debug(f"Вызов mask_card_number: {card_number}"))
        str_number = str(card_number)
        if len(str_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")

        masked_number = \
            f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"
        logger.info(f"Успешное маскирование карты. Результат: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"Ошибка в mask_card_number: {str(e)}", exc_info=True)
        return None


# Инициализация логирования при импорте модуля
setup_logging()
