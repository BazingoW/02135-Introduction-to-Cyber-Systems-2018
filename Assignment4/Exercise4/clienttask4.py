# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:58:30 2018

@author: Benjy
"""


import json
import requests
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
    r = requests.get("http://192.168.4.1/sensors/Temperature", headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'})
    rloaded = json.loads(r.text)
    file.write(str(round(time.time()-start))+","+str(rloaded[name])+";\n")

#r = requests.get(192.168.41:80)

    
file.close()

