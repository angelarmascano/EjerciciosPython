# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 21:28:47 2022

@author: Compaqi5
"""

def smart_thermostat(temp, people_in):
    if temp == 20 and people_in == True:
       action = "Caleraccon encendida"
    elif temp == 23 and people_in == False:
       action = "Encender termostato"      
    else: 
       action = "No hacer nada"  
    print ( "La acción es {0} ".format(action))

smart_thermostat(24,False)
