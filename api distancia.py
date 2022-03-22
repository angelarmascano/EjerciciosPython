# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:26:33 2022

@author: Compaqi5
"""



import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = '8ca3PsKmjeElnA7c78LvG9RXJNzOOfS8'
#Replace con la clave de MapQuest" #Replace con la clave de MapQuest
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
