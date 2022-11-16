# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:32:10 2021

@author: lenovo
"""

user_word = input("Enter a word (10 characters)")
if not(user_word.isdigit()):
    if len(user_word) > 10:
        print(f"{user_word} is too long")
    elif len(user_word) < 10:
        print(f"{user_word'} is not long eno'ugh")


print(user_word[0])
print(user_word[len(user_word)-1])

print(user_word[0])
print(user_word[1])
print(user_word[2])
print(user_word[3])
print(user_word[4])
print(user_word[5])
print(user_word[6])
print(user_word[7])
print(user_word[8])
print(user_word[9])

import random
random.shuffle(user_word)
