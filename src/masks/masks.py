from . import masks_logger


def mask_card_number(card_number: str) -> str:
    try:
        (masks_logger.debug
         (f"Вызвана функция mask_card_number с номером: {card_number}"))
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Некорректный номер карты")

        masked = \
            f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        masks_logger.info(f"Номер карты успешно замаскирован: {masked}")
        return masked
    except Exception as e:
        (masks_logger.error
         (f"Ошибка при маскировании номера карты: {str(e)}", exc_info=True))
        raise
