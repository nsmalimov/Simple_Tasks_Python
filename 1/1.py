#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os 
import sys
from nltk import regexp_tokenize
from Stemmer import Stemmer

directory = sys.argv[1]; 

files = os.listdir(directory); 

text_file = filter(lambda x: x.endswith('.txt'), files); 

all_text = ""

for i in text_file:
    try:
      f = open(i, 'r')
      all_text = all_text + f.read()
    except:
      print i
stm = Stemmer('russian')
text = stm.stemWords(regexp_tokenize((all_text.decode('UTF-8')).lower(), r"(?x) \w+ | \w+(-\w+)*"))
for i in text:
    num = text.count(i)
    print i.encode('UTF-8'), " ", num

      

