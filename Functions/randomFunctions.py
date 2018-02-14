#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging												## System module
log = logging.getLogger(__name__)

from random import randint

import requests
import json

import Functions.message as ms										    ## Own module




def flipCoinFunction():
    coin = randint(1, 6000)
    if coin < 3000:
        return ms.flipHead
    elif coin > 3000:
        return ms.flipTail
    return ms.flipEdge


def randomNumberFunction(number=11):
    log.info(number)
    return randint(0, number)


def forwardedMessageFunction(message):
    forwardMessage = message['forward_from']
    return str(forwardMessage)[1:-1].replace(',', '\n')


def shortLinkFunction(link, token):
    params = json.dumps({'longUrl':link})
    headers = {'content-type': 'application/json'}

    url = '{0}?key={1}'.format('https://www.googleapis.com/urlshortener/v1/url', token)

    response = requests.post(url, data=params, params=None, headers=headers, verify=True, timeout=5)
    if response.ok:
        try:
            data = response.json()

        except ValueError as e:
            return (False, e)
        if 'id' in data:
            return (True, data['id'])

    return (False, "Error Desconocido")



log.info('RandomFunctions Module Loaded.')
