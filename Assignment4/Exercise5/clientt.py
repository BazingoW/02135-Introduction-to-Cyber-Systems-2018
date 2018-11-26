# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:58:30 2018

@author: Benjy
"""


import json
import requests
import time


while True:
    print("Welcome to the danger zone")
    inp = input()
    barred = inp.replace(" ","/")
    send = "http://192.168.4.1/"+barred+"/"
    r = requests.get(send)