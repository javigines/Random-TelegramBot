#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @randomutils_bot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#

import logging												## System module
log = logging.getLogger(__name__)

import logging												## System module
log = logging.getLogger(__name__)

from uuid import uuid4                                      ## System module
import re

from telegram import InlineQueryResultArticle, InputTextMessageContent

import Functions.randomFunctions as rf                      ## Own module
import Functions.basicData as bd                            ## Own module

shortLink = True


def inlinequery(bot, update):
    global shortLink

    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Flip",
            description="Flip a Coin",
            input_message_content=InputTextMessageContent(
                 rf.flipCoinFunction())
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Random",
            description="Random number 0 to 10",
            input_message_content=InputTextMessageContent(
                 rf.randomNumberFunction())
        )
    ]
    if shortLink:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', query)
        if len(urls) > 0:
            state, shortLink = rf.shortLinkFunction(urls[0], bd.shorterGoogleToken)
            if state:
                results.append(
                    InlineQueryResultArticle(
                        id=uuid4(),
                        title="Shortlink",
                        description="Pulsame y te lo devolveré acortado",
                        input_message_content=InputTextMessageContent(shortLink)))
            else:
                bd.exceptionHandler(bot, update, __name__, shortLink, query)


    update.inline_query.answer(results, cache_time=1)

if bd.shorterGoogleToken == '':
    try:
        token_file = open("token.txt", 'r')
        bd.shorterGoogleToken = token_file.read().splitlines()[1]
    except Exception as e:
        bd.exceptionHandler(bot, update, __name__, "Ha ocurrido un error en la lectura del token de google, " + str(e), args)
        shortLink = False
    token_file.close()



log.info('InlineCommands Module Loaded.')
