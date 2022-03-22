# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:14:44 2022

@author: Compaqi5
"""
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("Ingrese el número para generar serie Fibonacci: "))

# first two terms
n1, n2 = 0, 1
count = 0


if nterms == 1:
   print(n1)
else:
   print("Fibonacci Secuencia:")
   while count < nterms:
       print(n1)
       sum = n1 + n2       
       n1 = n2
       n2 = sum
       count += 1