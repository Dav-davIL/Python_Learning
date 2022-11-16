# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 20:51:07 2021

@author: lenovo
"""

user_number = input("Please enter a number: ")
if user_number.isdigit():
    if int(user_number)%2 == 0:
        print(user_number, " is even")
    else:
        print(user_number, " is odd")