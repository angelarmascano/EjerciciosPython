# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:53:00 2022

@author: Compaqi5
"""

def esta_en_rango(rango, numero):
    return numero in range(*rango)

z=esta_en_rango([1,11], 10)
print (z)