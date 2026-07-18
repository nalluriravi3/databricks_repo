import logging

class Logger:
    def get_logger(logger_name, log_file):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        if logger.hasHandlers():
            logger.handlers.clear()

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler(log_file)       
        file_handler.setFormatter(formatter)       
        logger.addHandler(file_handler)

        return logger