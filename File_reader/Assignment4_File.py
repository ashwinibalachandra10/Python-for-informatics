#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 05:49:10 2022
@author: Ashwini Balachandra

Write a 
program that prompts the user for a filename. Open the file, and read it one line at a time. Do 
not use hard-coded file paths in your program, and do not require the user to specify the path. 
Instead, use the %cd magic command in your IPython console (magic commands can only be 
used in an IPython console; you can't use them in a .py file) to position yourself in the code3 
directory. Now run your program, ask the user for the filename, and then open and read it. For 
each line split the line into a list of words called file_word_list. For each word in the current 
file_word_list, convert the word to lowercase and look to see if it is in a list called script_list (a 
list that is initially empty). If the word is not in script_list, add it to the script_list. Sort the 
script_list alphabetically. 
2. Within the same program define a function called freq_count(). This function accepts a str and a 
list of words as arguments. [Note: str is a Python object type. Hence, you should never use str as 
an identifier. str already refers to the string class object, and by using the name str to refer to 
something else, you lose the ability to reference the string class object str! Instead, you can use 
str as a compositional element in an identifier name, such as search_str.]  I would name my 
arguments, search_str and word_list, respectively. But that’s just because I like my variable 
names to tell me what they represent, and why I am using them. Note that are careful to avoid 
confusion by using two different names, file_word_list and word_list. These variables are 
created and used in different scopes, and we don’t want to delude ourselves into thinking that 
they are the same variable—so we give them different names. Your freq_count() function 
traverses the list of words (word_list) and searches each word and counts the occurrences of 
the substring (search_str) within each word. To perform this substring search, you must use the 
find(...) method, and you should use the find(...) method is a manner that allows you to specify 
the position at which the substring search begins within the string. For this assignment, you 
are not allowed to use the string count() method or the re.findall(...) method to obtain your 
counts. Instead, you must use the string find(...) method. Hint: try specifying the starting 
position of your find operation by passing the starting position in as a variable—i.e., use two 
arguments when you call the find(...) method. The freq_count() function should print each 
word along with the number of substring occurrences found within the associated word. 
Please note that you are not counting the number of occurrences in the list or in the file! Your 
counts are counts within the words—each unique and separate word, that is, not all of the 
words! 
3. Modify this same program so that it accepts the filename and the substring str as input from the 
user. After reading the file to build and sort the script_list, pass the script_list into a call of the 
freq_count() function.
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
