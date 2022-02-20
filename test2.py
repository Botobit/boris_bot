#! /bin/python3

import urllib.request
import re
from urllib.parse   import quote

#search = input('what?\n')
#search2 = search.replace(' ','+')
#print(search2)
#search3 = 'https://www.youtube.com/results?search_query='+search
#print(search3)
word = 'приколы и хохмы'
word1 = word.replace(' ','+')

html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + quote(word1))
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print(video_ids)
