# logger.py

import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter("%(asctime)s - %(message)s")

log_handler = RotatingFileHandler(
    "activity_log.txt", maxBytes=100000, backupCount=5, encoding='utf-8'
)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger("weather_calc_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(log_handler)

def log_event(message):
    # Replace Unicode symbols with ASCII equivalents
    cleaned = message.replace("→", "->").replace("°", " deg")
    logger.info(cleaned)
