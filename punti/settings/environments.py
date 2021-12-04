ENV_NAME = 'LOCAL'  # GET FROM FILE

ENVIRONMENTS = {
    'LOCAL': {
        'mongo': {
            'host': '127.0.0.1',
            'port': 27015,
        }
    }
}

ENV = ENVIRONMENTS[ENV_NAME]
