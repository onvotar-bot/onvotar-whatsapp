import os
import logging

from aiotg import Bot, Chat
from onvotar import calculate

bot = Bot(
        api_token=os.environ.get("API_TOKEN"),
        name=os.environ.get("BOT_NAME"),
        )


AJUT_CAT = (
    'Per conèixer el teu col·legi electoral, '
    'envia un missatge /vota amb les teves dades '
    'separades per espais i '
    'fent servir aquest format: \n'
    '/vota DNI DATA_NAIXEMENT CODI_POSTAL\n\n'
    'Exemple:\n/vota 00001714N 01/10/2017 01234'
)

AJUT_CAST = (
    'Para conocer tu colegio electoral, '
    'envía un mensaje /votar con tus datos '
    'separados por espacios y '
    'usando este formato: \n'
    '/vota DNI DATA_NACIMIENTO CODIGO_POSTAL\n\n'
    'Ejemplo:\n/votar 00001714N 01/10/2017 01234'
)

AJUT_ENG = (
    'To know you voting booth location, '
    'send a message /vote with your data '
    'separated with spaces, using  '
    'this format: \n'
    '/vote DNI BIRTH_DATE ZIP_CODE\n\n'
    'Example:\n/vote 00001714N 01/10/2017 01234'
)

AJUT_OC = (
    'Per conéisser lo tieu collègi electoral, envia un messatge '
    '/vòta amb las tiás donadas separadas per espacis e en '
    'emplegant aquel format: \n'
    '/vòta DNI DATA_NAISSENÇA CÒDI_POSTAL\n\n'
    'Exemple:\n'
    '/vòta 00001714N 01/10/2017 01234'
)


@bot.command(r'/ajuda_oc')
async def ajuda_oc(chat: Chat, match):
    await chat.send_text(AJUT_OC)

@bot.command(r'/ajuda')
async def ajuda(chat: Chat, match):
    await chat.send_text(AJUT_CAT)

@bot.command(r'/ayuda')
async def ajuda_es(chat: Chat, match):
    await chat.send_text(AJUT_CAST)

@bot.command(r'/help')
async def ajuda_en(chat: Chat, match):
    await chat.send_text(AJUT_ENG)


@bot.command(r'/start')
async def ajuda(chat: Chat, match):
    await chat.send_text("Votar 1 Octubre Bot: /ajuda o /ajuda_oc o /ayuda or /help")

def filter_text(dni, cp, dnaix):
    dni = dni.upper().replace(' ','').replace('-','')
    dnaix = dnaix.upper().replace(' ','').replace('/','')
    dnaix = dnaix[-4:]+dnaix[2:4]+dnaix[:2]
    return (dni,cp,dnaix)

#@bot.command(r'/vota (\d{8}[A-Z]) (\d{5}) (\d{2})/(\d{2})/(\d{4})')

@bot.command(r'/vota (\d{8}[A-Z]) (\d{2}/\d{2}/\d{4}) (\d{5})')
@bot.command(r'/votar (\d{8}[A-Z]) (\d{2}/\d{2}/\d{4}) (\d{5})')
@bot.command(r'/vote (\d{8}[A-Z]) (\d{2}/\d{2}/\d{4}) (\d{5})')
@bot.command(r'/vòta (\d{8}[A-Z]) (\d{2}/\d{2}/\d{4}) (\d{5})')
async def vota(chat: Chat, match):
    dni = match.group(1)
    cp = match.group(3)
    dnaix = match.group(2)
    dni, cp, data = filter_text(dni, cp, dnaix)
    result = calculate(dni, data, cp)
    await chat.send_text(result)

@bot.default
def default(chat, message):
    return chat.send_text("Votar 1 Octubre Bot: /ajuda o /ayuda or /help")
