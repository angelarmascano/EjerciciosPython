# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:27:12 2022

@author: Compaqi5
"""

def Fibonacci(n):
   

    if n < 0:
        print("Entrada incorrecta")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 

print(Fibonacci(3))