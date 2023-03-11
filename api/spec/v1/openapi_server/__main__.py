#!/usr/bin/env python3

import connexion
from api.spec.v1.openapi_server import encoder

import api.spec.v1.logging_config.config as logging_config


def main():
    logging_config.init()
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'User API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
