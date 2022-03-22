# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:09:19 2022

@author: Compaqi5
"""

try:
    y=1/0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Aritmetic problem")
print("FIN")