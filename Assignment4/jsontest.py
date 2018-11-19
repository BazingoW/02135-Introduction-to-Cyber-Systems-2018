# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:24:41 2018

@author: Benjy
"""

pin_name = "Pin1"
import json

pin1 = "pin1"

pins = ["Pin1","Pin2","Pin3"]

sensors = ["Sensor1","Sensor2","Temperature"]

temp = "Temperature"


pinsdict = {}
for i in pins:
    pinsdict[i] = 1
    
dumped = json.dumps(pinsdict)

pin1 = {pin_name:pinsdict[pin_name]}

pin1dumped = json.dumps(pin1)

pinsdict = {}
for i in pins:
    pinsdict[i] = 1
    
    
sensorsdict = {}
for i in sensors:
    sensorsdict[i] = 1
    
sensorsdumped = json.dumps(sensorsdict)

temp1 = {temp:sensorsdict[temp]}

temp1dumped = json.dumps(temp1)