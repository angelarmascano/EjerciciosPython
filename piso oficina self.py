# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:42:51 2022

@author: Compaqi5
"""


class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = floor_numbers
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        print(self._type_to_number_dict)
        
    def ask_which_floor(self, floor_type):    
        if floor_type in self._floor_types:
            print('The {} floor is the number: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('There is no {} floor in this building.'.format(floor_type))
    
    def go_to_floor(self, floor_number):
        if floor_number in self._floor_numbers:
            print("Yendo a {} Piso ".format(self._number_to_type_dict[floor_number]))
        else:
            print("No existe el piso {} en este edificio. ".format(floor_number))
            
floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas'] 
floor_numbers = range(-1,4)

el = Elevator(floor_numbers, floor_types)

#el.go_to_floor(4)
el.ask_which_floor('Negocios')

            
           