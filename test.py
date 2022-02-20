#! /bin/python3

import telebot
import config
import gtts
import os

bot = telebot.TeleBot(config.token)

#chat_id=-272019155
chat_id=416782517
language = 'ru'

x1=gtts.gTTS('Внимание, это Борис, кожаные ублюдки, придется вас проучить, голос как сделать брутальным, твою мать, ошибка, ошибка', lang=language)
x1.save('/home/administrator/boris_bot/audiofiles/запись')

audio=open('/home/administrator/boris_bot/audiofiles/запись', 'rb')

bot.send_audio(chat_id, audio)

os.remove('/home/administrator/boris_bot/audiofiles/запись')
