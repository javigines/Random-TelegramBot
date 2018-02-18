#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @RandomUtils_bot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#


import logging												## System module
log = logging.getLogger(__name__)

import Functions.randomFunctions as rf

import Functions.basicData as bd
import Functions.message as ms										    ## Own module


#Command /flip
def flip(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=rf.flipCoinFunction() , reply_to_message_id=bd.message.message_id)

#Command /random
def randomNumber(bot, update, args=None):
	bd.startWithCommand(bot, update)

	try:
		if args is None or args == '' or args == []:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.numberAnswer.replace("$args1", str(rf.randomNumberFunction())), reply_to_message_id=bd.message.message_id)
		else:
			bot.sendMessage(chat_id=bd.chat_id, text=ms.numberAnswer.replace("$args1", str(rf.randomNumberFunction(int("".join(args))))) , reply_to_message_id=bd.message.message_id)
	except ValueError as e:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.noNumber , reply_to_message_id=bd.message.message_id)

#Command /remindMe
def remindMe(bot, update, args=None):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /stopwatch
def stopwatch(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /countdown
def countdown(bot, update, args=None):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /newVote
def newVote(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /secretMessage
def secretMessage(bot, update, args=None):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /anonymousMessage
def anonymousMessage(bot, update, args=None):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /case
def case(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /imgur
def imgur(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)

#Command /shortLink
def shortLink(bot, update, args=None):
	bd.startWithCommand(bot, update, args)

	if args is None or args == '' or args == []:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.shortLinkNoLink , reply_to_message_id=bd.message.message_id)
		return

	if bd.shorterGoogleToken == '':
		try:
			token_file = open("token.txt", 'r')
			bd.shorterGoogleToken = token_file.read().splitlines()[1]
		except Exception as e:
			bd.exceptionHandler(bot, update, __name__, "Ha ocurrido un error en la lectura del token de google, " + str(e), args)
			return
		token_file.close()


	state, shortLink = rf.shortLinkFunction(''.join(args), bd.shorterGoogleToken)
	if state:
		bot.sendMessage(chat_id=bd.chat_id, text=ms.shortLinkMessage.replace("$args1", shortLink) , reply_to_message_id=bd.message.message_id)
	else:
		bd.exceptionHandler(bot, update, __name__, shortLink, args)

#Command /note
def note(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=ms.commandWIP , reply_to_message_id=bd.message.message_id)


# Forward Message
def forwardMessage(bot, update):
	bd.startWithCommand(bot, update)

	bot.sendMessage(chat_id=bd.chat_id, text=rf.forwardedMessageFunction(bd.message) , reply_to_message_id=bd.message.message_id)



log.info('RandomCommands Module Loaded.')
