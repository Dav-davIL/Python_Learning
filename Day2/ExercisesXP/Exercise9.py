# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:16:35 2021

@author: lenovo
"""

user_tall = input("Please enter your tall (in inches)")
if user_tall.isdigit():
    user_tall *= 2.54
    if user_tall > 145:
        print("states they are tall enough to ride")
    else:
        print("they need to grow some more to ride.")