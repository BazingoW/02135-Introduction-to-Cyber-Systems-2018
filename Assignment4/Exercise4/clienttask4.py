# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:58:30 2018

@author: Benjy
"""


import json
import time

start = time.time()

end = time.time()+10

interval = 1

name = "Temperature"
temp = '{"Temperature": 1}'


file = open("temperaturelog.txt","w+")
file.write("Time,Temperature (celsius);\n")

print(time.time()>end)
while time.time()<end:
    time.sleep(interval)
    file.write(str(round(time.time()-start))+","+str(json.loads(temp)[name])+";\n")
    
    
    
file.close()

