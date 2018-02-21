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

from telegram import InlineQueryResultArticle, InputTextMessageContent

import Functions.randomFunctions as rf                      ## Own module
import Functions.basicData as bd                            ## Own module


def inlinequery(bot, update):
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

    update.inline_query.answer(results, cache_time=1)

log.info('InlineCommands Module Loaded.')
