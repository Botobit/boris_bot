#! /bin/python3
import telebot
import config
import requests, os, re
import random
import urllib.request
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve

bot = telebot.TeleBot(config.token)
chat_id=416782517
#chat_id=-272019155
slova = "dorime enigma"
slovax = slova.replace(' ','+')
zaprostext ="https://ru.hitmotop.com/search?q="+ slovax
data=requests.get(zaprostext, headers={'User-Agent': 'Mozilla/5.0'}).text
soup = bs(data, "html.parser")
tag = soup.find_all(href=re.compile("mp3"))
x = [url['href'] for url in tag]
x = str(x[0])
urlretrieve(x,"/home/administrator/boris_bot/files/" + slova)
getmusic = open('/home/administrator/boris_bot/files/' + slova, 'rb')
bot.send_audio(chat_id, getmusic)
os.remove('/home/administrator/boris_bot/files/' + slova)
#bot.send_message(chat_id,tube3)
