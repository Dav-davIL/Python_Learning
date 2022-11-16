# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:11:04 2021

@author: lenovo
"""

user_name = input("please enter your name: ")
if not(user_name.isdigit()):
	if user_name == 'david':
		print("we have the most beautiful name")
	else:
		print("david is prettier than ",user_name),