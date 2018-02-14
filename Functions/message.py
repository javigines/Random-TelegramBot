#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging												## System module
log = logging.getLogger(__name__)


# Command /help or /start
helpOrStart = ('Las funciones y comandos del bot son los siguiente:\n\n'+
				'/birthday 23/01/1997 - Añade tu cumpleaños al bot\n'+
				'/birthdayList (january|18/01/2017|2017)) - Listado de todos los cumpleaños o de los que se encuentren en la fecha.\n'+
				'/changelog - Últimos cambios en actualizaciones del bot\n'+
				'/contact ExampleMessage - Manda tu mensaje/sugerencia/bug al desarrollador.\n' +
				'/eventList (january|18/01/2017|2017) - Listado de todos los eventos o de los que se encuentren en la fecha.\n'+
				'/help - Esta ayuda\n'+
				'\n'+
				'Admin Commands\n'+
				'/event Título del Evento | Fecha del Evento con Hora y Duración. Formato:(17/06/2017 18:45 +04:30) | (Impartido por) | (Descripción del Evento) | (Precio del Evento)\n'+
				'- En el comando /event campos opcionales no usados dejarlos en blanco pero con los separadores |\n'+
				'/removeB @Peter - Borra el cumpleaños de la persona definida\n'+
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
