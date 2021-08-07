import logging
import consts


def initialize_logger():
    logger = logging.getLogger(consts.LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(f'{consts.LOG_FILE_NAME}.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logger_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logger_formatter)
    logger.addHandler(console_handler)
    return logging.getLogger(consts.LOGGER_NAME)

