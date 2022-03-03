#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:24:02 2022

@author: Ashwini
"""

#import string
fhand = open('mbox.txt')
msg_freq = dict()

for line in fhand:
    if line.startswith('From:') : 
        #line = line.translate(str.maketrans('','',string.punctuation))
        line = line.lower()
        words = line.split()
        
        print(words)

        if words[1] not in msg_freq:
          msg_freq[words[1]] = 1
        else:
           msg_freq[words[1]] += 1
        print(msg_freq)
# Sort the dictionary by value
lst = list()
for key, val in msg_freq.items():
    lst.append( (val, key) )
    lst.sort(reverse = True)
for key, val in lst[:10] :
    print(key, val)

print( 'The person with the highest number of sent messages is:', lst[0][1] ,' with ', lst[0][0], 'messages')