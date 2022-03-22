# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:25:39 2022

@author: Compaqi5
"""

switch=[]
lista=["R1", "R2", "R3", "R4", "R5", "S6", "S7" ]
for item in lista:
    if "S" in item:
        switch.append(item)
    
print(switch)