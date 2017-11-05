#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Commands.flipCoin as flipC

import Functions.basicData as bd


#Command /flip
def flip(bot, update):
	startWithCommand(bot, update)

	bot.sendMessage(chat_id=chat_id, text=flipC.flipCoinAnswer , reply_to_message_id=message.message_id)

#Command /getInfo
def getInfo(bot, update):
	startWithCommand(bot, update)

#Command /randomNumer
def randomNumer(bot, update, args=None):
	startWithCommand(bot, update)

#Command /remindMe
def remindMe(bot, update, args=None):
	startWithCommand(bot, update)

#Command /stopwatch
def stopwatch(bot, update):
	startWithCommand(bot, update)

#Command /newVote
def newVote(bot, update):
	startWithCommand(bot, update)

#Command /secretMessage
def secretMessage(bot, update, args=None):
	startWithCommand(bot, update)

#Command /anonymousMessage
def anonymousMessage(bot, update, args=None):
	startWithCommand(bot, update)

#Command /case
def case(bot, update):
	startWithCommand(bot, update)

#Command /imgur
def imgur(bot, update):
	startWithCommand(bot, update)

#Command /shortLink
def shortLink(bot, update):
	startWithCommand(bot, update)

#Command /note
def note(bot, update):
	startWithCommand(bot, update)
