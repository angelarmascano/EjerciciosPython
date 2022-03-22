# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:53:44 2022

@author: Compaqi5
"""

floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1,3)
elevator_dict = dict(zip(floors_numbers, floor_types)) 
print(elevator_dict)
print(elevator_dict[-1])
