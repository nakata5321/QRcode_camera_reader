import logging
import os
import time
import yaml
from src.QRcode_scanner import QR_scanner
from threading import Thread

def read_configuration() -> dict:

    config_path = dirname + '/config/config.yaml'
    logging.debug(config_path)

    try:
        with open(config_path) as f:
            content = f.read()
            config = yaml.load(content, Loader=yaml.FullLoader)
            logging.debug(f"Configuration dict: {content}")
            return config
    except Exception as e:
        while True:
            logging.error("Error in configuration file!")
            logging.error(e)
            exit()


if __name__ == '__main__':
    dirname = os.path.dirname(os.path.abspath(__file__))
    QR_scanner()
