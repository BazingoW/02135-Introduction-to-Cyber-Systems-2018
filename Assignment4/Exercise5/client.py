
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
time.sleep(interval)
r = requests.post("http://192.168.4.1/set", data={"LedRed/'p.;io,lumikp.;o,limkyujn":True})
rloaded = json.loads(r.text)
file.write(str(round(time.time()-start))+","+str(rloaded[name])+";\n")

#r = requests.get(192.168.41:80)

    
file.close()

