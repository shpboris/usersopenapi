import logging.config
import yaml
import os


def init():
    absolute_path = os.path.dirname(__file__)
    relative_path = "logging.yaml"
    full_path = os.path.join(absolute_path, relative_path)
    print("Log config path is: " + full_path)
    with open(full_path, 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
