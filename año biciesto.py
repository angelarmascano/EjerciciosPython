# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:01:49 2022

@author: Compaqi5
"""

def biciesto(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
print(biciesto(1900))
print(biciesto(2020))