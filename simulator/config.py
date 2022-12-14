#!/usr/bin/python3
import sys
import os
import json
import logging
import logging.config

import yaml


class Token:

    def __init__(self, token, address, decimals):
        self.token = token
        self.address = address
        self.decimals = decimals

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token


def get_int(hex_str):
    return int(hex_str, 16)


MODE = os.environ.get('KYBER_ENV', 'dev')
try:
    with open('config.yml', 'r') as f:
        cfg = yaml.load(f)

        logging.config.dictConfig(cfg['logging'])

        DELAY = cfg[MODE]['delay']
        BLOCKCHAIN_URL = cfg[MODE]['blockchain_url']

        try:
            with open(cfg[MODE]['addresses'], 'r') as f:
                addr = json.loads(f.read())

                EXCHANGES_ADDRESS = addr['exchangesAddress']
                for k, v in EXCHANGES_ADDRESS.items():
                    EXCHANGES_ADDRESS[k] = get_int(v)

                BANK_ADDRESS = get_int(addr['bank'])
                SUPPORTED_TOKENS = {}
                for name, token in addr['tokens'].items():
                    name = name.lower()
                    SUPPORTED_TOKENS[name] = Token(name,
                                                   get_int(token['address']),
                                                   token['decimals'])
        except FileNotFoundError as e:
            sys.exit('Deployment file is missing.')

except FileNotFoundError:
    sys.exit('Config file is missing.')


EXCHANGE_INFO = {}
for exchange in ['binance', 'bittrex', 'huobi']:
    with open("info/{}.json".format(exchange), 'r') as f:
        EXCHANGE_INFO[exchange] = json.loads(f.read())


SECRET = b'vtHpz1lUQTwUTz5p6VrxcEslF4KnDI21s1'
LOGGER_NAME = "simulator"
EXCHANGE_NAME = "liqui"

API_KEY = {
    'liqui': 's7kwmscu-u6myvpjh-47evo234-y2uxw61t-raxby17f',
    'binance': 'bbpcycmIbqJmudPrqeDzrt9CkY7nnl2ljvpRJ8CVenhejyhsyTBKQJ76BlDflR1K',
    'bittrex': '665ab1c6a04d4e4b855bd13639520c0a',
    'huobi': '48c32ba6-a86f961a-48fa19f1-bdbdc'
}

PRIVATE_KEY = {
    'bittrex': '7e72df544ce569ccd35b53a2e8411aaefebad8bb42b2ef443593663b1979ac9b',
    'liqui': '96cc6fb5cd1266f36d3c180bce8c5e4c34bd7577cad6a21fa4d59fb8589d8c28',
    'huobi': '628fee3875f87594b24c773ca410c5e5e25ad142bf2eef5ea9fc56018064fbad',
    'binance': 'cf0994187eedbeb765dd931372b75d542fd121577911486605352b32c1764b1e',
    'bitfinex': 'be0a3d742ee009b1cc7e69abcaa4dc9a5960a4bcbe0c55a11b1333826bcc13cc'
}

if MODE == 'ropsten':
    INITIAL_BALANCE = {
        'binance': {
            'bat': 100000,
            'elf': 100000,
            'eos': 100000,
            'eth': 100000,
            'gto': 100000,
            'knc': 100000,
            'mana': 100000,
            'omg': 100000,
            'powr': 100000,
            'req': 100000,
            'snt': 100000
        }
    }
else:
    INITIAL_BALANCE = {
        'bittrex': {
            'bat': 16554.708,
            'elf': 6254.464,
            'eos': 1260.1556,
            'eth': 63.26388,
            'gto': 24004.78,
            'knc': 2194.2484,
            'mana': 55340.4,
            'omg': 708.2968,
            'powr': 14092.964,
            'req': 38073.08,
            'snt': 49400.04,
            'rdn': 2396.6764,
            'appc': 9635.912,
            'eng': 2817.8472,
            'salt': 1945.8252            
        },
        'huobi': {
            'bat': 16554.708,
            'elf': 6254.464,
            'eos': 1260.1556,
            'eth': 63.26388,
            'gto': 24004.78,
            'knc': 2194.2484,
            'mana': 55340.4,
            'omg': 708.2968,
            'powr': 14092.964,
            'req': 38073.08,
            'snt': 49400.04,
            'rdn': 2396.6764,
            'appc': 9635.912,
            'eng': 2817.8472,
            'salt': 1945.8252
        },
        'binance': {
            'bat': 16554.708,
            'elf': 6254.464,
            'eos': 1260.1556,
            'eth': 63.26388,
            'gto': 24004.78,
            'knc': 2194.2484,
            'mana': 55340.4,
            'omg': 708.2968,
            'powr': 14092.964,
            'req': 38073.08,
            'snt': 49400.04,
            'rdn': 2396.6764,
            'appc': 9635.912,
            'eng': 2817.8472,
            'salt': 1945.8252
        }
    }
