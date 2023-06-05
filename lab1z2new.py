# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:26:09 2023

@author: t-jan
"""

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
from math import log

# Wczytaj pliki
with open('hamlet.txt', 'r') as file:
    hamlet = file.read()
with open('KingLear.txt', 'r') as file:
    kinglear = file.read()
with open('Othello.txt', 'r') as file:
    othello = file.read()
with open('RomeoJuliet.txt', 'r') as file:
    romeo = file.read()

# Podziel teksty na słowa
words_h = word_tokenize(hamlet)
words_k = word_tokenize(kinglear)
words_o = word_tokenize(othello)
words_r = word_tokenize(romeo)

# Lematyzacja słów
lemmatizer = WordNetLemmatizer()
for i in range (0,len(words_h)):
    words_h[i]=lemmatizer.lemmatize(words_h[i])
for i in range (0,len(words_k)):
    words_k[i]=lemmatizer.lemmatize(words_k[i])
for i in range (0,len(words_o)):
    words_o[i]=lemmatizer.lemmatize(words_o[i])
for i in range (0,len(words_r)):
    words_r[i]=lemmatizer.lemmatize(words_r[i])

# Zamień duże litery na małe
for word in range(0,len(words_h)):
    words_h[word]=words_h[word].lower()
for word in range(0,len(words_k)):
    words_k[word]=words_k[word].lower()
for word in range(0,len(words_o)):
    words_o[word]=words_o[word].lower()
for word in range(0,len(words_r)):
    words_r[word]=words_r[word].lower()

# Usuń stop words i słowa o długości <= 2
with open('stop_words_english.txt', 'r') as file:
    stop_words = file.read()
filtered_words_h = [word for word in words_h if word not in stop_words and len(word) > 2]
filtered_words_k = [word for word in words_k if word not in stop_words and len(word) > 2]
filtered_words_o = [word for word in words_o if word not in stop_words and len(word) > 2]
filtered_words_r = [word for word in words_r if word not in stop_words and len(word) > 2]

# Policz słowa
unique_words_h=Counter(filtered_words_h).keys() # equals to list(set(words))
counter_h=Counter(filtered_words_h).values() # counts the elements' frequency
unique_words_h=list(unique_words_h)
counter_h=list(counter_h)
unique_words_k=Counter(filtered_words_k).keys()
counter_k=Counter(filtered_words_k).values()
unique_words_k=list(unique_words_k)
counter_k=list(counter_k)
unique_words_o=Counter(filtered_words_o).keys()
counter_o=Counter(filtered_words_o).values()
unique_words_o=list(unique_words_o)
counter_o=list(counter_o)
unique_words_r=Counter(filtered_words_r).keys()
counter_r=Counter(filtered_words_r).values()
unique_words_r=list(unique_words_r)
counter_r=list(counter_r)

# Policz TF-IDF dla każdego unikalnego słowa w każdym dokumencie
tf_h=[]
tf_k=[]
tf_o=[]
tf_r=[]
idf_h=[]
idf_k=[]
idf_o=[]
idf_r=[]
tfidf_h=[]
tfidf_k=[]
tfidf_o=[]
tfidf_r=[]
len_h=sum(counter_h)
len_k=sum(counter_k)
len_o=sum(counter_o)
len_r=sum(counter_r)
for i in range(0,len(unique_words_h)):
    tf_h.append(counter_h[i]/len_h)
    d=1
    word=unique_words_h[i]
    if word in unique_words_k:
        d+=1
    if word in unique_words_o:
        d+=1
    if word in unique_words_r:
        d+=1
    idf_h.append(log(4/d))
    tfidf_h.append(tf_h[i]*idf_h[i])
for i in range(0,len(unique_words_k)):
    tf_k.append(counter_k[i]/len_k)
    d=1
    word=unique_words_k[i]
    if word in unique_words_h:
        d+=1
    if word in unique_words_o:
        d+=1
    if word in unique_words_r:
        d+=1
    idf_k.append(log(4/d))
    tfidf_k.append(tf_k[i]*idf_k[i])
for i in range(0,len(unique_words_o)):
    tf_o.append(counter_o[i]/len_o)
    d=1
    word=unique_words_o[i]
    if word in unique_words_h:
        d+=1
    if word in unique_words_k:
        d+=1
    if word in unique_words_r:
        d+=1
    idf_o.append(log(4/d))
    tfidf_o.append(tf_o[i]*idf_o[i])
for i in range(0,len(unique_words_r)):
    tf_r.append(counter_r[i]/len_r)
    d=1
    word=unique_words_r[i]
    if word in unique_words_h:
        d+=1
    if word in unique_words_o:
        d+=1
    if word in unique_words_k:
        d+=1
    idf_r.append(log(4/d))
    tfidf_r.append(tf_r[i]*idf_r[i])

# Wyodrębnij najlepsze słowa wg TF-IDF
words_tfidf_hamlet=[]
words_tfidf_kinglear=[]
words_tfidf_othello=[]
words_tfidf_romeo=[]

hzip = list(zip(tfidf_h, unique_words_h))
hzip.sort(reverse=True)
kzip = list(zip(tfidf_k, unique_words_k))
kzip.sort(reverse=True)
ozip = list(zip(tfidf_o, unique_words_o))
ozip.sort(reverse=True)
rzip = list(zip(tfidf_r, unique_words_r))
rzip.sort(reverse=True)

for i in range(0,500):
    for j in range(0,int(10000*tfidf_h[i]+1)):
        words_tfidf_hamlet.append(unique_words_h[i])
for i in range(0,500):
    for j in range(0,int(10000*tfidf_k[i]+1)):
        words_tfidf_kinglear.append(unique_words_k[i])
for i in range(0,500):
    for j in range(0,int(10000*tfidf_o[i]+1)):
        words_tfidf_othello.append(unique_words_o[i])
for i in range(0,500):
    for j in range(0,int(10000*tfidf_r[i]+1)):
        words_tfidf_romeo.append(unique_words_r[i])

# Zapisz oczyszczone słowa wg tfidf w pliku
with open('tfidf_hamlet.txt', 'w') as file:
    for word in words_tfidf_hamlet:
        file.write(word + '\n')
with open('tfidf_kinglear.txt', 'w') as file:
    for word in words_tfidf_kinglear:
        file.write(word + '\n')
with open('tfidf_othello.txt', 'w') as file:
    for word in words_tfidf_othello:
        file.write(word + '\n')
with open('tfidf_romeo.txt', 'w') as file:
    for word in words_tfidf_romeo:
        file.write(word + '\n')


