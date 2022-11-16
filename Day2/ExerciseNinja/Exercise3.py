# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:48:44 2021

@author: lenovo
"""
3 <= 3 < 9                         # ==> True
3 == 3 == 3                        # ==> True
bool(0)                             # ==> False
bool(5 == "5")                      # ==> True
bool(4 == 4) == bool("4" == "4")    # ==> true
bool(bool(None))                    # ==> False
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)        # ==> true
print("y is", y)        # ==> False
print("a:", a)          # ==> 5
print("b:", b)          # ==> 10