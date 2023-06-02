import os.path
import time
import logging
from logging.handlers import TimedRotatingFileHandler

from colorlog import ColoredFormatter
from app.config import config

LOGFILE = config.logger.LOGFILE
CLEAR_PERIOD_DAYS = config.logger.CLEAR_PERIOD_DAYS
LOG_IN_FILE = config.logger.LOG_IN_FILE


def clear_old_logs():
    """
    Функция очистки лог файла через заданное количество дней
    """
    if not os.path.exists(LOGFILE):
        return

    last_clear_time = os.path.getmtime(LOGFILE)
    current_time = time.time()

    if (current_time - last_clear_time) >= CLEAR_PERIOD_DAYS * 24 * 60 * 60:
        open(LOGFILE, 'w').close()

# Очищаем лог, если он старый
clear_old_logs()


logger = logging.getLogger(__name__)

LOGFORMAT = "%(log_color)s[%(levelname)s] %(asctime)s - %(message)s (%(filename)s:%(lineno)d)%(reset)s"
LOG_LEVEL = config.logger.LEVEL
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT, datefmt='%Y-%m-%d %H:%M:%S')
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
logger.setLevel(LOG_LEVEL)
logger.addHandler(stream)

# Включение записи в файл, если разрешено в конфигурации
if LOG_IN_FILE:
    LOGFORMAT = "[%(levelname)s] %(asctime)s - %(message)s (%(filename)s:%(lineno)s)"
    formatter = logging.Formatter(LOGFORMAT, datefmt='%Y-%m-%d %H:%M:%S')
    handler = TimedRotatingFileHandler(LOGFILE, when="d", interval=30)
    handler.setFormatter(formatter)
    logger.addHandler(handler)






