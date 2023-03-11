import logging.config
import yaml


def init():
    with open('../logging_config/logging.yaml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
