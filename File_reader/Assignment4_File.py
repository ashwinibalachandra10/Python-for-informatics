#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 05:49:10 2022
@author: Ashwini Balachandra
"""

def freq_count(search_str, word_list):
    for word in word_list :
        count = 0
        pos = word.find(search_str)
        while pos >= 0:
            count += 1
            pos += len(search_str)        
            pos = word.find(search_str,pos)
        print( word +  str(count))

fname = input('Enter the filename:')
search_str = input('Enter substring :')

try:
    fhand = open(fname)
except:
    print('File cannot be open :',fname)
    exit()
    
script_list =[]
for line in fhand:
   file_word_list = line.split()
   for word in file_word_list:
       word_lower = word.lower()
       if word_lower not in script_list:
           script_list.append(word_lower)
           script_list.sort()
          
print(script_list)
freq_count(search_str,script_list)
