#! /bin/python3
import config
import telebot, bs4, requests
import os, urllib.request
import random
import socket
import requests.packages.urllib3.util.connection as urllib3_cn
from lxml import html
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import wikipedia
from bs4 import BeautifulSoup as bs
import gtts
from urllib.parse import quote
from mg import get_map_cell


bot = telebot.TeleBot(config.token)
cols, rows = 8, 8

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row( telebot.types.InlineKeyboardButton('←', callback_data='left'),
			  telebot.types.InlineKeyboardButton('↑', callback_data='up'),
			  telebot.types.InlineKeyboardButton('↓', callback_data='down'),
			  telebot.types.InlineKeyboardButton('→', callback_data='right') )

maps = {}

@bot.message_handler(func=lambda message: 'поставь' in message.text.lower(), content_types=['text'])
def songbot(message):
    song = message.text.lower()
    startsong = song.find('поставь')
    songword=song[startsong+8:]
    slovax = songword.replace(' ','+')
    zaprostext ="https://ru.hitmotop.com/search?q="+ slovax
    data=requests.get(zaprostext, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = bs(data, "html.parser")
    tag = soup.find_all(href=re.compile("mp3"))
    x = [url['href'] for url in tag]
    x = str(x[0])
    urlretrieve(x,"/home/administrator/boris_bot/files/" + songword)
    getmusic = open('/home/administrator/boris_bot/files/' + songword, 'rb')
    bot.send_audio(message.chat.id, getmusic)
    os.remove('/home/administrator/boris_bot/files/' + songword)

@bot.message_handler(func=lambda message: 'покажи' in message.text.lower(), content_types=['text'])
def kartinkabot(message):
    kartinka=message.text.lower()
    startzapros=kartinka.find('покажи')
    slovo=kartinka[startzapros+7:]
    zapros ="https://images.rambler.ru/search?query="+ slovo
    data=requests.get(zapros, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup = bs(data, "html.parser")
    tag = soup.find_all('meta', property="og:image")
    for url in tag:
        x = (url['content'])
        try:
            urlretrieve(x,"/home/administrator/boris_bot/files/picture.png")
            sendpic = open('/home/administrator/boris_bot/files/picture.png', 'rb')
            bot.send_photo(message.chat.id, sendpic)
            os.remove('/home/administrator/boris_bot/files/picture.png')
        except:
            bot.send_message(message.chat.id, 'я не хочу это показывать')

@bot.message_handler(func=lambda message: 'скажи' in message.text.lower(), content_types=['text'])
def voicebot(message):
    textsay=message.text.lower()
    startsay=textsay.find('скажи')
    say2=textsay[startsay+6:]
    say1=gtts.gTTS(say2, lang='ru')
    say1.save('/home/administrator/boris_bot/audiofiles/Борис в эфире')
    audio=open('/home/administrator/boris_bot/audiofiles/Борис в эфире', 'rb')
    bot.send_audio(message.chat.id, audio)
    os.remove('/home/administrator/boris_bot/audiofiles/Борис в эфире')

@bot.message_handler(func=lambda message: 'найди видео' in message.text.lower(), content_types=['text'])
def tubeurl(message):
    textsearch=message.text.lower()
    startsearch=textsearch.find('найди видео')
    tube2=textsearch[startsearch+12:]
    tube2=tube2.replace(' ','+')
    tube1="https://www.youtube.com/results?search_query="+ quote(tube2)
    try:
        htmltube=urllib.request.urlopen(tube1)
        videopart=re.findall(r"watch\?v=(\S{11})", htmltube.read().decode())
        tube3="https://www.youtube.com/watch?v="+videopart[0]
        bot.send_message(message.chat.id,tube3)
    except:
        bot.send_message(message.chat.id,'Не охота что-то, давай в другой раз')

@bot.message_handler(func=lambda message: 'что такое' in message.text.lower(), content_types=['text'])
def wiki_module(message):
    wikipedia.set_lang('ru')
    text=message.text.lower()
    start=text.find('что такое')
    termin=text[start+10:]
    try:
        x=wikipedia.summary(termin, sentences=3)
        bot.send_message(message.chat.id,x)
    except:
        bot.send_message(message.chat.id,'Не врубился, что за херню ты спрашиваешь')

@bot.message_handler(func=lambda message: '/opredelenie' in message.text.lower(), content_types=['text'])
def wiki_module2(message):
    wikipedia.set_lang('ru')
    text=message.text.lower()
    start=text.find('/opredelenie')
    termin=text[start+13:]
    try:
        x=wikipedia.summary(termin, sentences=3)
        bot.send_message(message.chat.id,x)
    except:
        bot.send_message(message.chat.id,'Не врубился, что за херню ты спрашиваешь')

@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(message.chat.id, 'руки убери, кожаный мешок')

@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Укуси мой блестящий металлический зад!')

def getpicsay():
    xwords=('ахаха)))', 'ю-ху-ху', 'круто!', 'все, тормози, хорош', 'удоли', 'воу-воу))', 'За тобой уже выехали', 'пошла жара!', 'о, годнота подъехала', 'woop woop its a sound of da police')
    xmix=(random.sample(xwords, k=1))
    return xmix

@bot.message_handler(content_types=["photo"])
def handle_for_picture(message):
    bot.reply_to(message, getpicsay())

#@bot.message_handler(content_types=["sticker"])
#def send_sticker(message):
#    sticker_id = message.sticker.file_id
#    bot.reply_to(message, sticker_id)

def monetkasay():
    stik1=('CAACAgIAAxkBAAIRz2HEJoSfr7h_gAZUoxgHZUnPb08sAAKHDAAC8tooSyR335kyJlnhIwQ')
    stik2=('CAACAgIAAxkBAAIRzWHEJoS0ZmxSs-jz_Uv9TfPgK0joAALwCwACqfAgSxfWwiTgkCYVIwQ')
    stik3=('CAACAgIAAxkBAAIRy2HEJoMwhX47UFD1bTGFFUAQ8rTUAAK7DAACwCUgS8H3b-09ZxmNIwQ')
    stik4=('CAACAgIAAxkBAAIRyWHEJoIDdaSYJmxhCXb7eqRP733aAAKZCwAC9d_ISvHG4XNDmpXpIwQ')
    stik5=('CAACAgIAAxkBAAIRx2HEJoAkfQ353EPAe8N_1ObDJTFQAALYCwACWA-YSjT4-vW-cVivIwQ')
    stik6=('CAACAgIAAxkBAAIRxWHEJoCmoI0dNPAobWZM8X9oUlNlAAJ2CAACFnFYSitaMA-qUubEIwQ')
    stik7=('CAACAgIAAxkBAAIRw2HEJnucZuB8eTyzb98e5ipFElZlAALICwACbUKgSvbfy2r2RSkGIwQ')
    stik8=('CAACAgIAAxkBAAIRwWHEJnoVE2We1bh6Sq5uGge6a6pYAAI2CwACnKKYSm2f8xD1_AFpIwQ')
    stik9=('CAACAgIAAxkBAAIRv2HEJngP4WD4z2o927jvxzQ0cHu6AAK5DgACA42QSo3ipMt0F5UiIwQ')
    stik10=('CAACAgIAAxkBAAISVmHETPLdUZsDUwqFjvEUh8mDP8W6AAJcCwACDY5ASurM0V75mxhFIwQ')
    stik11=('CAACAgIAAxkBAAISWGHETZaEiQvhVww1TVg98MQur1TeAAKZCwAC9d_ISvHG4XNDmpXpIwQ')
    mes=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
    mixmes=(random.sample(mes, k=1))
    if 'a' in mixmes:
        return stik1
    elif 'b' in mixmes:
        return stik2
    elif 'c' in mixmes:
        return stik3
    elif 'd' in mixmes:
        return stik4
    elif 'e' in mixmes:
        return stik5
    elif 'f' in mixmes:
        return stik6
    elif 'g' in mixmes:
        return stik7
    elif 'h' in mixmes:
        return stik8
    elif 'i' in mixmes:
        return stik9
    elif 'j' in mixmes:
        return stik10
    elif 'k' in mixmes:
        return stik11

def monetkasay2():
    mwords=('ОРЕЛ', 'РЕШКА')
    mimix=(random.sample(mwords, k=1))
    return mimix

@bot.message_handler(func=lambda message: '/luckycoin' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'подкинь' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'монет' in message.text.lower(), content_types=['text'])
def handle_for_monetka(message):
    bot.send_sticker(message.chat.id, monetkasay())
    bot.reply_to(message, monetkasay2())

@bot.message_handler(func=lambda message: 'boris' in message.text.lower(), content_types=['text'])
def handle_messagenametwo(message):
    bot.reply_to(message, 'Ублюдок, мать твою, а ну иди сюда, говно собачье! А? Сдуру решил ко мне лезть?! Ты, засранец вонючий, мать твою, а? Ну, иди сюда,﻿ попробуй меня трахнуть, я тебя сам трахну, ублюдок, онанист чертов')

@bot.message_handler(func=lambda message: 'троекратное' in message.text.lower(), content_types=['text'])
def handle_messagevmf(message):
    bot.send_message(message.chat.id, 'Ура! Ура! Ура!')

@bot.message_handler(func=lambda message: '/chat_number' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'абракадабра' in message.text.lower(), content_types=['text'])
def numberchat(message):
    bot.send_message(message.chat.id, 'номер этого чата {!s}'.format(message.chat.id))

@bot.message_handler(func=lambda message: 'молодец' in message.text.lower(), content_types=['text'])
def handle_messagevmf(message):
    bot.send_message(message.chat.id, 'Рад служить, хозяин')

def getanekdot():
    z=''
    s=requests.get('http://anekdotme.ru/random')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.anekdot_text')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s

@bot.message_handler(func=lambda message: '/anekdot' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'анекдот' in message.text.lower(), content_types=['text'])
def handle_anymessage(message):
    bot.reply_to(message, getanekdot())

def getpicture():
    urllib3_cn.allowed_gai_family = lambda: socket.AF_INET
    url='https://www.images.reseto.com/random.php'
    data=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    soup=BeautifulSoup(data,"xml")
    images=[image['src'] for image in soup.find_all(src=re.compile("jpg"))]
    for img in images:
        urlretrieve(img,"/home/administrator/boris_bot/files/local-filename.png")

@bot.message_handler(func=lambda message: '/mem' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'мем' in message.text.lower(), content_types=['text'])
def mem_message(message):
    getpicture()
    ximg = open('/home/administrator/boris_bot/files/local-filename.png', 'rb')
    bot.send_photo(message.chat.id, ximg)
    os.remove('/home/administrator/boris_bot/files/local-filename.png')

def getweather():
    z=''
    s=requests.get('https://a-weather.ru/place/ru-ekaterinburg/tomorrow/')
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.weather_about')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s

@bot.message_handler(func=lambda message: '/pogodavoice' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'погода голосом' in message.text.lower(), content_types=['text'])
def weather_voice(message):
    weathersay1=gtts.gTTS(getweather(), lang='ru')
    weathersay1.save('/home/administrator/boris_bot/audiofiles/Погода')
    weathersay2=open('/home/administrator/boris_bot/audiofiles/Погода', 'rb')
    bot.send_audio(message.chat.id, weathersay2)
    os.remove('/home/administrator/boris_bot/audiofiles/Погода')

@bot.message_handler(func=lambda message: '/pogoda' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'погода' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'погоду' in message.text.lower(), content_types=['text'])
def weather_message(message):
    bot.reply_to(message, getweather())

def getcitato():
    z=''
    s=requests.get('https://quote-citation.com/random',headers={'User-Agent': 'Mozilla/5.0'})
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.quote-text')
    for x in p:
        s=(x.getText().strip())
        z=z+s+'\n\n'
    return s

@bot.message_handler(func=lambda message: '/citato' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'цитат' in message.text.lower(), content_types=['text'])
@bot.message_handler(func=lambda message: 'боря' in message.text.lower(), content_types=['text'])
def citato_message(message):
    bot.reply_to(message, getcitato())

@bot.message_handler(func=lambda message: 'случайное число' in message.text.lower(), content_types=['text'])
def randomizer(message):
    rantext=message.text.lower()
    if 'случайное число' in rantext and 'от' in rantext and 'до' in rantext:
        ot=rantext.find('от')
        do=rantext.find('до')
        f_num=int(rantext[ot+3:do-1])
        l_num=int(rantext[do+3:])
        bot.reply_to(message, str(random.randint(f_num, l_num)))
    else:
        bot.reply_to(message, 'Ну кто так вводит, введи, например, случайное число от 1 до 10')

def getsis():
    urllib3_cn.allowed_gai_family = lambda: socket.AF_INET
    HEADER = {
    'Host': 'tits-guru.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://tits-guru.com/randomTits',
    'Connection': 'keep-alive',
    'Cookie': 'PLAY_LANG=en; partner_v3=true',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'cross-site',
    'Cache-Control':'max-age=0',
    }

    URL = "https://tits-guru.com/randomTits"
    r = requests.get(URL,headers=HEADER)
    soup = bs(r.text, "html.parser")
    urly = soup.find_all('a', class_="img-link fancybox")
    for url in urly:
        z=url.img['src']
        storage="/home/administrator/boris_bot/xfiles/x.png"
        os.system('wget -O {0} {1}'.format(storage,z))

@bot.message_handler(func=lambda message: '/adult' in message.text.lower(), content_types=['text'])
def mem_sis(message):
    getsis()
    ximge = open('/home/administrator/boris_bot/xfiles/x.png', 'rb')
    bot.send_photo(message.chat.id, ximge)
    os.remove('/home/administrator/boris_bot/files/local-filename.png')

##################################game######################################
def get_map_str(map_cell, player):
	map_str = ""
	for y in range(rows * 2 - 1):
		for x in range(cols * 2 - 1):
			if map_cell[x + y * (cols * 2 - 1)]:
				map_str += "❎"
			elif (x, y) == player:
				map_str += "⛹"
			elif x == cols * 2 - 2 and y == rows * 2 - 2:
				map_str += "⭕"
			else:
				map_str += "⬜"
		map_str += "\n"

	return map_str

@bot.message_handler(commands=['play'])
@bot.message_handler(func=lambda message: 'игру' in message.text.lower(), content_types=['text'])
def play_message(message):
	map_cell = get_map_cell(cols, rows)

	user_data = {
		'map': map_cell,
		'x': 0,
		'y': 0
	}

	maps[message.chat.id] = user_data
	bot.send_message(message.from_user.id, 'Дорогой геймер, если ты с телефона, то советую перевернуть горизонтально. В этой игре ты играешь за юного Майкла Джордана (еще в те времена, когда он был белым). Ты должен пройти через лабиринт судьбы и заскочить в красное кольцо, став тем самым звездой NBA.')
	bot.send_message(message.from_user.id, get_map_str(map_cell, (0, 0)), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
	user_data = maps[query.message.chat.id]
	new_x, new_y = user_data['x'], user_data['y']

	if query.data == 'left':
		new_x -= 1
	if query.data == 'right':
		new_x += 1
	if query.data == 'up':
		new_y -= 1
	if query.data == 'down':
		new_y += 1

	if new_x < 0 or new_x > 2 * cols - 2 or new_y < 0 or new_y > rows * 2 - 2:
		return None
	if user_data['map'][new_x + new_y * (cols * 2 - 1)]:
		return None

	user_data['x'], user_data['y'] = new_x, new_y

	if new_x == cols * 2 - 2 and new_y == rows * 2 - 2:
		bot.edit_message_text( chat_id=query.message.chat.id,
							   message_id=query.message.id,
							   text="Ты победил, черт возьми, ты сделал это! Майкл Джордан стал в итоге королем баскетбола и больше не знал в жизни проблем, за исключением первого брака, нескольких эпизодов с наркотиками и парочки штрафов за неправильную парковку." )
		return None

	bot.edit_message_text( chat_id=query.message.chat.id,
						   message_id=query.message.id,
						   text=get_map_str(user_data['map'], (new_x, new_y)),
						   reply_markup=keyboard )

############################################################################
bot.polling(none_stop=False, interval=0)


if __name__ == '__main__':
	bot.infinity_polling()
