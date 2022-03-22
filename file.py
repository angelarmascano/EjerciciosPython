# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:39:06 2022

@author: Compaqi5
"""

file=open("devices.txt")
for item in file:
    item=item.strip()
    print(item)
file.close()