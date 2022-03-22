# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:04:12 2022

@author: Compaqi5
"""

def GetDomain(email):
    print(email.split("@")[-1])
GetDomain('user@domain.com')
