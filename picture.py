#! /bin/python3
import telebot
import config
import requests, os
import random
import urllib.request
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve

bot = telebot.TeleBot(config.token)
chat_id=416782517
#chat_id=-272019155
slovo ="редис"
zapros ="https://images.rambler.ru/search?query="+ slovo
data=requests.get(zapros, headers={'User-Agent': 'Mozilla/5.0'}).text
soup = bs(data, "html.parser")
tag = soup.find_all('meta', property="og:image")
for url in tag:
    x = (url['content'])
    urlretrieve(x,"/home/administrator/boris_bot/files/picture.png")
    sendpic = open('/home/administrator/boris_bot/files/picture.png', 'rb')
    bot.send_photo(chat_id, sendpic)
    os.remove('/home/administrator/boris_bot/files/picture.png')

#bot.send_message(chat_id,tube3)
