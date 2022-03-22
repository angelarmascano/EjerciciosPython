# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:57:37 2022

@author: Compaqi5
"""

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784 
    # 1 mile = "1.60934" meters
    # 1 km   = 1000 meters .. 1000 * 1.60934 = 1609.344
    # 100km = 100 * 1000 meters (The function works on 100 km)
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km_100 = miles * 1609.344 * 1000 / 100
    liters = 3.785411784
    return liters / km_100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))