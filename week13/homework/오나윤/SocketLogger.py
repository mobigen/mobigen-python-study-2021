import logging.config
import configparser
import logging.handlers as handlers
import os

def singleton(cls):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return get_instance()

@singleton
class SocketLogger():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'settings.conf'))
        #log
        logger = logging.getLogger('logger')
        log_path = config.get('log','log_path')
        log_file_name = config.get('log','log_file_name')
        maxBytes = config.getint('log','maxBytes')
        backupCnt = config.getint('log','backupCount')
        log_level = config.get('log','log_level')

        # check if log directory exists
        if os.path.isdir(log_path) is False:
                os.makedirs(log_path)

        log_file_path = log_path + log_file_name
        logger.setLevel(int(log_level))
        logHandler = handlers.RotatingFileHandler(log_file_path, maxBytes=maxBytes, backupCount=int(backupCnt))
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        self.logger = logger
