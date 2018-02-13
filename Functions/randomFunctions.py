#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging												## System module
log = logging.getLogger(__name__)

from random import randint

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


log.info('RandomFunctions Module Loaded.')
