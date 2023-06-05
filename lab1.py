# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 09:39:21 2023

@author: t-jan
"""

from nltk.tokenize import word_tokenize

# Wczytaj plik
with open('hamlet.txt', 'r') as file:
    text = file.read()

# Podziel tekst na słowa
words = word_tokenize(text)

# Zamień duże litery na małe
for word in range(0,len(words)):
    words[word]=words[word].lower()

# Usuń stop words i słowa o długości <= 2
with open('stop_words_english.txt', 'r') as file:
    stop_words = file.read()
filtered_words = [word for word in words if word not in stop_words and len(word) > 2]

# Zapisz oczyszczone słowa w pliku
with open('oczyszczone_slowa.txt', 'w') as file:
    for word in filtered_words:
        file.write(word + '\n')

