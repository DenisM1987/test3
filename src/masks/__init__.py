import logging
from pathlib import Path

# Создаем папку logs, если её нет
logs_dir = Path(__file__).resolve().parent.parent.parent / "logs"
logs_dir.mkdir(exist_ok=True)

# Настройка логгера для masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

# Обработчик для записи в файл
file_handler = logging.FileHandler(logs_dir / "masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Форматтер
file_formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
masks_logger.addHandler(file_handler)
