# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 12:56:00 2022

@author: lenovo
"""

import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

# display the hidden word
word_length = len(word)
space_index = word.find(" ")
if space_index != -1:
    word_1 = word[0] + (space_index-2) * "_" + word[space_index-1]
    word_2 = word[space_index+1] + (word_length-space_index-3) * "_" + word[-1]
    word_hidden = word_1 + " " + word_2
else:
    word_hidden = word[0] + (word_length-2) * '_' + word[-1]
word_hidden_list = list(word_hidden)
print(word_hidden)

# ask to the user to choose a letter
user_value_used_list = []
UnderscoreNumber = word_length - 2
tryIndex = 0
while (UnderscoreNumber > 0 and tryIndex <= 6):
    user_value = input("Please, choose a letter: ")
    user_value = user_value.lower()
    position = 0
    #check if the user has already used this value
    user_value_used_str = "".join(user_value_used_list)
    userValueIndex = user_value_used_str.find(user_value)
    if userValueIndex == -1:
        user_value_used_list.append(user_value)
        user_value_times = word.count(user_value)
        #check the position value
        if user_value_times > 0:
            for x in range(user_value_times):
                position = word.find(user_value,position+1,word_length)
                if position != -1:
                    word_hidden_list[position] = user_value
                    word_hidden = "".join(word_hidden_list)
        else:
            if tryIndex >= 6:
                print(" ==========Y= ")
            if tryIndex >= 5:
                print(" ||/       |  ")
            if tryIndex >= 4:
                print(" ||        0  ")
            if tryIndex >= 3:
                print(" ||       /|\ ")
            if tryIndex >= 2:
                print(" ||       /|\  ")
            if tryIndex >= 1:                    
                print("/||           ")
            if tryIndex >= 0:
                print("==============\n")
            tryIndex += 1
            if tryIndex > 6:
                print("Game Over !!")
                break
    else:
        print("This value is alreadu used")
    UnderscoreNumber = word_hidden.count("_")
    print(word_hidden)
if UnderscoreNumber == 0:
    print("Bravo !!")
