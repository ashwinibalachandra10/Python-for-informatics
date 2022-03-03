#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:22:40 2022
@author: Ashwini Balachandra

Description:
Count the number of characters received (read), and stop displaying any text after it has shown 
exactly 3000 characters. Space characters, tab characters, and newline characters are 
characters, and should therefore be included in your count. All of your processing is in terms of 
chunks. So, you are not allowed to count or print character by character. Instead, you must 
increment your count by the size of the chunk of characters that you read. That size will always 
be equal to your default chunk size, except for the very last chunk that you read from the file. 
The last chunk that you read from the file will likely be less than your default chunk size. Since 
your chunk size will not divide evenly into 3000, you will need to add some logic to ensure that 
exactly 3000 characters (no more, and no less) are displayed. When you print your chunks, it is 
okay for them to be separated by a newline character. Do not use magic numbers! The values 
3000 and 512 should be established as named constants. In Python, the convention is to name a 
constant by using an identifier in all caps: e.g., PRINT_LIMIT = 3000. Any other values that you 
might use should be derived from these two named constants. The idea is for to allow for the 
values 3000 and 512 to be adjusted (to 5000 and 256, for example), and still ensure that your 
code operates correctly. 
Very important! You are not allowed to calculate manually or programmatically the number of 
iterations needed to reach your 3000 character print limit. In other words, instead of counting 
iterations (or divisions), you need to count the number of characters that you have read so far. 
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
