#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4
from random import randint									## System module

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent

import Commands.flipCoin as flipC

import Functions.basicData as bd


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Flip",
            description="Flip a Coin",
            input_message_content=InputTextMessageContent(
                 flipC.flipCoinAnswer())
        )
    ]

    update.inline_query.answer(results, cache_time=1)
