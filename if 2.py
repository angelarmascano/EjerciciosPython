# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:25:46 2022

@author: Compaqi5
"""

acl=int(input("Ingrese la Edad: "))
if acl>=3 and acl <=6:
    print("de 4 a 6 Es un niño de Pre escolar")
elif acl>=6 and acl<=12:
    print("de 7 a 12 Es un joven de escuela")
elif acl>=12 and acl<=18:
    print("de 13 a 18 Es un joven de colegio")
elif acl>=18 and acl<=26:
    print("de 19 a 26 Es un joven de universidad")
else:
    print("más de 26 Es un joven en su vida laboral")