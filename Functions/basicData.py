#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)
from sys import exc_info

import Functions.message as ms


## Debug chat_id
chatIDDeveloper = 372406715

## Usefull Variables
message = None
username = None
chat_id = None
user_id = None


def startWithCommand(bot, update, args=['']):
	global message
	global username
	global chat_id
	global user_id

	if update.message == None:
		message = update.edited_message
	else:
		message = update.message

	username = message.from_user.name
	chat_id = message.chat.id
	user_id = message.from_user.id

	log.info(message.text.split(' ')[0] + ' ' + ' '.join(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")
	bot.sendMessage(chat_id=chatIDDeveloper, text=message.text.split(' ')[0] + ' ' + ' '.join(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")")

def userNotAuthorizedMessage(bot, update, args=['']):
	bot.sendMessage(chat_id=chatIDDeveloper, text=ms.userNotAuthorizedCommand.replace("$args1",
	message.text.split(' ')[0] + ' ' + ' '.join(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")"))

def exceptionHandler(bot, update, nameModule, exception, args=['']):
	log.error(str(exception)+ " - Module: " + nameModule + " Line "+ str(exc_info()[2].tb_lineno))
	bot.sendMessage(chat_id=chat_id, text=ms.errorExecCommandUser, reply_to_message_id=message.message_id)
	bot.sendMessage(chat_id=chatIDDeveloper, text=ms.errorExecCommandAdmin.replace("$args1",
	message.text.split(' ')[0] + ' ' + ' '.join(args) + ' --> ' + username + " (chat_id:" + str(chat_id) + " , user_id:"+ str(user_id) + ")"))


def basicErrorTelegramHandler(bot, update, telegramError):
	log.error(str(telegramError))

log.info('BasicData Module Loaded.')
