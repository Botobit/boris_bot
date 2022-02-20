#! /bin/python3

import telebot
import config
import gtts
import os
import bs4, requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.token)

chat_id=-272019155
#chat_id=416782517

z=''
s=requests.get('https://a-weather.ru/place/ru-ekaterinburg/tomorrow/')
b=bs4.BeautifulSoup(s.text, "html.parser")
p=b.select('.weather_about')
for x in p:
    s=(x.getText().strip())
    z=z+s+'\n\n'

s3=s.replace("°C"," ")
s1=s3.split()

del s1[:7]
del s1[20:]

if int(s1[16])>=20:
    sayw="прекрасная летняя погодка"
elif int(s1[16])<20 and int(s1[16])>=10:
    sayw="ветровка согреет вашу душу"
elif int(s1[16])<10 and int(s1[16])>=0:
    sayw="скорее бы лето"
elif int(s1[16])<0 and int(s1[16])>=-10:
    sayw="теплее чем зимой, но спать на улице не стоит"
elif int(s1[16])<-10 and int(s1[16])>=-20:
    sayw="на улице конкретный такой дубак"
else:
    sayw="одевайте меховые портки, а лучше вообще из дома ни ногой"

s2=" ".join(s1)
sx=(s2 + sayw)

weathersay1=gtts.gTTS(sx, lang='ru')
weathersay1.save('/home/administrator/boris_bot/audiofiles/Погода')
weathersay2=open('/home/administrator/boris_bot/audiofiles/Погода', 'rb')
bot.send_audio(chat_id, weathersay2)
os.remove('/home/administrator/boris_bot/audiofiles/Погода')

