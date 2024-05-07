import inspect
import logging
from datetime import date


def get_logger():
    # Initialize the logger
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # Check first if there is no existing logger with the same name otherwise, return the existing one
    if not len(logger.handlers):
        # Set the name and directory of the log file
        date_today = date.today().strftime("%d-%m-%Y")
        file_handler = logging.FileHandler(f"resources/logs/logfile_{date_today}.log")
        # Configure the format of every log message
        formatter = logging.Formatter("%(asctime)s %(levelname)s - %(name)s: %(message)s", "%d-%B-%Y %I:%M:%S%p")
        file_handler.setFormatter(formatter)
        # Add the configured handler into the logger
        logger.addHandler(file_handler)
        # Set the minimum level of logging
        logger.setLevel(logging.DEBUG)

    return logger
