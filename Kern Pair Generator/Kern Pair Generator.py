#MenuTitle: Kern Pair Generator
# -*- coding: utf-8 -*-
__doc__="""
Tired of searching kernable words for specific kerning pairs? This script comes in handy.
"""


import vanilla
import GlyphsApp
from random import shuffle
import codecs

Variable([
    dict(name="Language", ui="PopUpButton", args=dict(items=['EN-Lat', 'FR-Lat', 'GU-Guj', 'GR-Gre', 'RU-Cyr'])),
    dict(name="Right", ui="EditText"),
    dict(name="Left", ui="EditText"),
    dict(name="Case", ui="PopUpButton", args=dict(items=['UC_UC', 'UC_lc', 'lc_lc'])),
    ], globals())
 
if Language == 0:
    with open('eng_news_2016_100K-words-UC.txt', 'r', encoding='utf-8') as f:
        words = 10000
        loadWords = [l[:-1] for l in f.readlines()]
        shuffle(loadWords)
        loadWords = loadWords[:words]
        
if Language == 1:
    with open('fra_mixed-typical_2012_100K-words.txt', 'r', encoding='utf-8') as f:
        words = 10000
        loadWords = [l[:-1] for l in f.readlines()]
        shuffle(loadWords)
        loadWords = loadWords[:words]
        
if Language == 2:
    with open('guj_newscrawl_2016_100K-words.txt', 'r', encoding='utf-8') as f:
        words = 10000
        loadWords = [l[:-1] for l in f.readlines()]
        shuffle(loadWords)
        loadWords = loadWords[:words]

if Language == 3:
    with open('ell_newscrawl_2017_100K-words.txt', 'r', encoding='utf-8') as f:
        words = 10000
        loadWords = [l[:-1] for l in f.readlines()]
        shuffle(loadWords)
        loadWords = loadWords[:words]
        
if Language == 4:
    with open('rus_newscrawl-public_2018_100K-words.txt', 'r', encoding='utf-8') as f:
        words = 10000
        loadWords = [l[:-1] for l in f.readlines()]
        shuffle(loadWords)
        loadWords = loadWords[:words]


lista = list(Right)
listb = list(Left)
output = []
finalWords = []

for x in range(len(lista)):
    for y in listb:
        output.append(lista[x] + y)
        
if Case == 0:
    for uc in range(len(output)):
        output[uc] = output[uc].upper()
    for ucw in range(len(loadWords)):
        loadWords[ucw] = loadWords[ucw].upper()
        
if Case == 1:
    for cp in range(len(output)):
        output[cp] = output[cp].capitalize()
    for cpw in range(len(loadWords)):
        loadWords[cpw] = loadWords[cpw].capitalize()

if Case == 2:
    for lc in range(len(output)):
        output[lc] = output[lc].lower()
    for lcw in range(len(loadWords)):
        loadWords[lcw] = loadWords[lcw].lower()
      

f = Glyphs.font

if f.currentTab == None:
    f.newTab()
f.currentTab.text = '  '.join(finalWords)