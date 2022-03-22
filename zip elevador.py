# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:07:45 2022

@author: Compaqi5
"""

floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1,3)
elevator=list(zip(floor_types, floors_numbers))
elevator1=list(zip(floors_numbers, floor_types))
print(elevator)
print(elevator[-1])



