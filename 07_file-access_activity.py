# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:36:19 2022

@author: iarmas
"""

file = open("devices.txt", "a")
while True:
        newitem = input('Ingrese el nuevo dispositivo: ')
        if newitem == 'q':
            file.close()
            file = open("devices.txt", "r")
            print(file.read())
            print("All done")
            break
        else:
           file.write(newitem + "\n") 