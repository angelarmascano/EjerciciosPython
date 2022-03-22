# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:50:38 2022

@author: Compaqi5
"""

def countIoT(st):
    count=0
    for word in st.lower().split():
        if word == 'iot':
            count += 1
    return count
    
count=countIoT('I don\'t know how to spell IoT ! Is it IoT or iot ? What does iot mean anyway?')
print(count)