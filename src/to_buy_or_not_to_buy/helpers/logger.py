import datetime
import logging
from typing import Optional


def create_logger(
    name: str = "default_logger", level: Optional[int] = logging.INFO
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        current_date_and_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{current_date_and_time}_{name}.log"

        file_handler = logging.FileHandler(file_name)
        file_handler.setLevel(level)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
