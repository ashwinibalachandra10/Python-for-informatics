#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:22:40 2022
@author: Ashwini Balachandra
"""

import urllib.request, urllib.parse, urllib.error

CHUNK_SIZE = 512
PRINT_LIMIT = 3000
try :
    INPUT_url = input ("Enter the Url to be read :")
    fhand = urllib.request.urlopen(INPUT_url)
except:
    print("Unable to open the Url")
    exit()


size = 0
count = 0
bytes_rem = PRINT_LIMIT
while True:
    data_content = fhand.read(CHUNK_SIZE)
    count = count + 1
    if len(data_content) < 1: 
        break
    size = size + len(data_content)
    if (size <= 3000):
        print(data_content.decode(),end='')
    if (size < 3000 and count == int(PRINT_LIMIT/CHUNK_SIZE)):
        data_content = fhand.read(PRINT_LIMIT%CHUNK_SIZE)
        size = size + len(data_content)
        print(data_content.decode(),end='')
        print( '\n', size, 'characters copied.End')
    
print ('\nTotal number of characters read: ', size)
fhand.close()
