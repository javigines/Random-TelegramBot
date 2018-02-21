#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides functionality to the @randomutils_bot
# Copyright (C) 2017-2018
# Javier Gines Sanchez <software@javisite.com>
#

import logging												## System module
log = logging.getLogger(__name__)


# Command /help or /start
helpOrStart = ('Las funciones y comandos del bot son los siguiente:\n\n'+
				'/anonymousMessage or /am - (WIP) _Mensaje anónimo para quien tu quieras que se lo mande._\n'+
				'/countdown or /cd - (WIP) _Cuenta atrás desde el valor que tú elijas._\n'+
				'/flip or /fl - _¿Cuántas veces has querido lanzar una moneda para echar algo a suertes? Este es tu comando. Comando Inline._\n'+
				'/help - _Esta ayuda._\n'+
				'/newvote or /nv - (WIP) _Te hago una votacion para que la envies._\n' +
				'/random (Número) or /rand - _Un número random del 0 al 10. Me puedes indicar un número y lo usaré como valor máximo. Comando Inline._\n'+
				'/remindme or /rm - (WIP) _Te envio una notificación en la fecha que me indiques._\n'+
				'/secretmessage or /sm - (WIP) _Envio un mensaje secreto entre tu y quien elijas._\n'+
				'/shortlink http://example.com or /sl - _Te acorto el link de la web que me mandes._\n'+
				'/stopwatch or /sw - (WIP) _¿Quieres un cronometro? Yo puedo servirte para eso._\n'+
				'\n'+
				'También puedo darte datos de interes de un usuario si me reenvias un mensaje suyo.\n'
				'\n'+
				'Admin Commands\n'+
				'/leave - _Si me encuentro en un grupo, lo abandono._\n'+
				'\n'+
				'/changelog - _Por si tienes interés, aquí tienes los últimos cambios realizados._\n'+
				'/contact - _¿Quieres contactar con el desarrollador? Escribe tu mensaje para que se lo envie._\n'+
				'\n'+
				'Un comando Inline significa que me puedes llamar desde cualquier chat escribiendo @randomutils\_bot y pulsando la opción que quieras de las que te aparezcan.\n'
				'\n'+
				'Todos los parámetros entre paréntesis son opcionales. En el caso de usarlos, no incluir el paréntesis.\n'
				)

#Command /restartP
restartWrongOS = "El bot tiene que estar corriendo sobre Linux para usar esta opción."
restarting = "Reiniciando..."

#Command /stopP
stopping = "Deteniendo..."

#Command /updateP
updateWrongOS = "El bot tiene que estar corriendo sobre Linux para usar esta opción."
updating = "Actualizando..."
updateDone = 'Actualización completa. Reinicia para aplicar.'

# Command /leave
leaving = "Hasta Siempre..."
notGroupLeave = "Este chat no permite el comando /leave"

# Command /changelog
changelogMessage = '$args1 $args2 \nPara ver el changelog completo:\nhttps://goo.gl/U4S72c'
groupChangelogUser = 'No queremos aburrir a la gente con el listado de cambios, ¿por qué no me lo preguntas por privado mejor?'

# Command /speakP & /contact
contactMessage = 'El usuario $args1 ($args2) te ha enviado un mensaje:\n$args3'
contactNoMessage = "Es necesario incluir un mensaje seguido del comando."
messageSend = 'Mensaje enviado.'
incorrectChatId = 'El chat_id indicado no es válido o no tengo acceso a él.'

# Command /downloadP
downloadNoArgs = "Es necesario introducir argumentos para realizar la descarga"
downloadInProgress = "Enviando Archivo..."
downloadComplete = "Archivo enviado."

# Command /clearLogP
clearlogComplete = "Archivo de log borrado."

# General Messages
errorExecCommandAdmin = 'Error al ejecutar $args1'
errorExecCommandUser = 'Ha ocurrido un error y se ha informado de él.'
userNotAuthorizedCommand = "Un usuario esta intentando usar un comando no autorizado:\n$args1"
notAdmin = ['No intentes hacer lo que no debes.',
			'Estás tocando algo que no debes, huye mientras puedas, es una amenaza.']
commandWIP = 'The command is not avalible yet, we are working in bring it as soon as possible.'


# Command or Inline /flip
flipEdge = "Era complicado pero lo conseguiste, ha caído de canto"
flipHead = "Cara"
flipTail = "Cruz"

# Command /random
numberAnswer = "Ha salido el $args1"
noNumber = "No has introducido un número válido"

# Command /shortLink
shortLinkMessage = "Aquí tienes tu link acortado: $args1"
shortLinkNoLink = "Tienes que introducir un link junto con el comando"


log.info('Message Module Loaded.')
