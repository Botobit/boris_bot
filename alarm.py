#! /bin/python3
import telebot
import config
import requests, re
import random
import urllib.request
from urllib.parse import quote

bot = telebot.TeleBot(config.token)
#chat_id=416782517
chat_id=-272019155

randwords=('chill', 'игры олдфагов', 'лсд', 'rock guitar', 'пелевин', 'квантовая механика', 'коля маню', 'таинственное', 'история рейв культуры')
tube2=(random.sample(randwords, k=1))
for y in tube2:
    y

tube2=y.replace(' ','+')
tube1="https://www.youtube.com/results?search_query="+ quote(tube2)
htmltube=urllib.request.urlopen(tube1)
videopart=re.findall(r"watch\?v=(\S{11})", htmltube.read().decode())
xx=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
x=(random.sample(xx, k=1))
for x1 in x:
    x1

tube3="https://www.youtube.com/watch?v="+videopart[x1]
#tube3="https://www.youtube.com/watch?v="+videopart[0]
bot.send_message(chat_id,tube3)
