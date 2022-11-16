# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:29:50 2021

@author: lenovo
"""

user_input = input("Please enter a month (1 to 12):")
if not(user_input.isdigit()):
    user_input = input("Please enter a month (1 to 12):")
else:
    if int(user_input) >=3 and int(user_input) <=5:
        print("Spring runs from March (3) to May (5)")
    elif int(user_input) >=6 and int(user_input) <=8:
        print("Summer runs from June (6) to August (8)")
    elif int(user_input) >=9 and int(user_input) <=11:
        print("Autumn runs from September (9) to November (11)")
    elif int(user_input) <=3 and int(user_input) >=1 or int(user_input) ==12:
        print("Winter runs from December (12) to February (2)")
        
