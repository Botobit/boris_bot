#! /bin/python3
import telebot
import config
import requests,bs4,re
import random
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup as bs

bot = telebot.TeleBot(config.token)
#chat_id=416782517
chat_id=-272019155

url='https://pikabu.ru/'
pikabu=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
htmlpikabu=bs(pikabu, 'html.parser')
links = [link['href'] for link in htmlpikabu.find_all('a', class_="story__title-link")]
n0=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n=(random.sample(n0, k=1))
for n1 in n:
    n1

result=links[n1]

bot.send_message(chat_id,result)

