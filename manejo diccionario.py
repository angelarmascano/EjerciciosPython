# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 18:19:39 2022

@author: Compaqi5
"""
d = {'k1':['val1','val2','val3',{'we':['need','to','go',{'deeper':[1,2,3,'that']}]}]}

d = {'k1':['val1','val2','val3',{'we':['need','to','go',{'deeper':[1,2,3,'that']}]}]}
print(d['k1'][3]['we'][3]['deeper'][3])
