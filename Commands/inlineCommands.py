#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4
from random import randint									## System module

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent

import Functions.randomFunctions as rf

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
