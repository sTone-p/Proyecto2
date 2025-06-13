from . import app_settings
import os
import logging
from logging.handlers import TimedRotatingFileHandler


LOG_FORMAT = '%(asctime)s - %(procces)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def configure_loggin():
    os.makedirs(app_settings.LOG_DIR, exist_ok=True)
    log_filename = f'{app_settings.LOG_DIR}/Gestor_api.log'

    log_level = logging.DEBUG if app_settings.DEBUG else logging.INFO

    file_handler = TimedRotatingFileHandler(log_filename, 'midnight', 1)
    file_handler.suffix = DATE_FORMAT   

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(LOG_FORMAT, DATETIME_FORMAT)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)

    console_handler.setLevel(logging.WARNING)
    root_logger.addHandler(console_handler)