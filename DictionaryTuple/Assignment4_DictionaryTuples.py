#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 22:24:02 2022
@author: Ashwini Balachandra

1.write a program that reads through the mail box data and when you find a line 
that starts with “From”, extract the address information from the line. Count the number of 
messages from each person by using a dictionary. Note that you might need to look at more 
than “From” because of duplicate instances of the address (hint: “From ” vs. “From:”, not both! 
If you search for “From”, you will find both “From ” and “From:”, which will erroneously double 
your count—please note that “From “ is not the same as “From”). Otherwise, embedded email 
“thread histories” may cause your count to be incorrect. In other words, when counting the 
message "sends", you definitely don't want to count any embedded messages that are included 
as part of the message thread history. The idea is to count "original" sends. If you send me a 
message, and I respond, you respond to my response, etc., etc.,... how many times did you send 
that original message? Only once, right? 
2. After all of the data has been read, print (i.e., print) a message to the user stating that the 
person with the highest number of sent messages is <email_address>, along with the number of 
sent messages associated with that email address (e.g., “with n messages”). In other words, as 
with any informatics output, your output should be meaningful—e.g., “The person with the 
highest number of sent messages is neo@matrix.com with 7700 messages.” To obtain your 
result, create a list of tuples (count, email) from the dictionary, sort the list in reverse ord er and 
print out the person who has the highest number of messages. The U in DSU does not mean 
that you print a list, and it doesn ́t mean that you print a tuple. Rather, it means that you 
Undecorate, i.e. extract the necessary information from the tuple and present it to the user in a 
meaningful form (something your boss will understand). 
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
