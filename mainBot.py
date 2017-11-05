#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Functions.basicCommands as bc
import Functions.randomCommands as rc

import Functions.inlineQuery as iq

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)


# Usefull for /restartB
if(len(argv)>1):
	sleep(2)
	call("kill -9 " + str(argv[1]), shell=True)
	sleep(2)


token_file = open("token.txt", 'r')
token = token_file.readline()
token_file.close()

updater = Updater(token, workers=200)
dispatcher = updater.dispatcher

# Initialize "Command" handlers
# Basic Commands
start_handler = CommandHandler(list(['start','help']), bc.start, pass_args=False, allow_edited=True)
dispatcher.add_handler(start_handler)
restart_handler = CommandHandler(list(['restartB','rebootB']), bc.restartB, pass_args=False, allow_edited=True)
dispatcher.add_handler(restart_handler)
stop_handler = CommandHandler('stopB', bc.stopB, pass_args=False, allow_edited=True)
dispatcher.add_handler(stop_handler)
leave_handler = CommandHandler('leaveB', bc.leaveGroup, pass_args=False, allow_edited=True)
dispatcher.add_handler(leave_handler)
update_handler = CommandHandler('updateB', bc.updateB, pass_args=False, allow_edited=True)
dispatcher.add_handler(update_handler)
changelog_handler = CommandHandler('changelog', bc.changelogB, pass_args=False, allow_edited=True)
dispatcher.add_handler(changelog_handler)

# Random Commands
flip_handler = CommandHandler('flip', rc.flip, pass_args=False, allow_edited=True)
dispatcher.add_handler(flip_handler)
getInfo_handler = CommandHandler('getInfo', rc.getInfo, pass_args=False, allow_edited=True)
dispatcher.add_handler(getInfo_handler)
randomNumer_handler = CommandHandler('randomNumer', rc.randomNumer, pass_args=False, allow_edited=True)
dispatcher.add_handler(randomNumer_handler)
remindMe_handler = CommandHandler('remindMe', rc.remindMe, pass_args=False, allow_edited=True)
dispatcher.add_handler(remindMe_handler)
stopwatch_handler = CommandHandler('stopwatch', rc.stopwatch, pass_args=False, allow_edited=True)
dispatcher.add_handler(stopwatch_handler)
newVote_handler = CommandHandler('newVote', rc.newVote, pass_args=False, allow_edited=True)
dispatcher.add_handler(newVote_handler)
secretMessage_handler = CommandHandler('secretMessage', rc.secretMessage, pass_args=False, allow_edited=True)
dispatcher.add_handler(secretMessage_handler)
anonymousMessage_handler = CommandHandler('anonymousMessage', rc.anonymousMessage, pass_args=False, allow_edited=True)
dispatcher.add_handler(anonymousMessage_handler)
case_handler = CommandHandler('case', rc.case, pass_args=False, allow_edited=True)
dispatcher.add_handler(case_handler)
imgur_handler = CommandHandler('imgur', rc.imgur, pass_args=False, allow_edited=True)
dispatcher.add_handler(imgur_handler)
shortLink_handler = CommandHandler('shortLink', rc.shortLink, pass_args=False, allow_edited=True)
dispatcher.add_handler(shortLink_handler)
note_handler = CommandHandler('note', rc.note, pass_args=False, allow_edited=True)
dispatcher.add_handler(note_handler)

# Random Inline
dispatcher.add_handler(InlineQueryHandler(iq.inlinequery))

updater.start_polling(timeout=30)
print("MainBot Completly Loaded.\nBot Working...")
updater.bot.sendMessage(chat_id=chatIDDeveloper, text="Bot Iniciado")

try:
    while 1:
        schedule.run_pending()
        sleep(1)
except (KeyboardInterrupt, TypeError):
    print("Exception")
finally:
    updater.idle()
    print("\nBot Stoped\nShuting down...")
