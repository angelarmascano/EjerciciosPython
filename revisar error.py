# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:49:23 2022

@author: Compaqi5
"""



    
def readint(promt,min,max):
   while True:
       num = raw_input("Escribe un numero entero: ")
       try:
           entrada = int(num)
           return num
       except ValueError:
           print ("La entrada es incorrecta: escribe un numero entero")
           
        if num > max:
            print('El número a ingresar no debe ser mayor que {} . el valor ingresado fue: {}'.format(max,num))
        if num > min:
            raise Exception('El número a ingresar no debe ser menor que {} . el valor ingresado fue: {}'.format(min,num))

    
readint("Hubo un error",-10,10)    
    
print("El número ingresado fue: ",num)