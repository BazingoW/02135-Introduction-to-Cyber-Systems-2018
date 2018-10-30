import machine
import neopixel
import time

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
listsensor = i2c.scan()
address = listsensor[0]
temp_reg = 5
res_reg = 8

#Neopixel colors (G,R,B)
# Red (0,255,0)
# Yellow (255,255,0)
#Green (255,0,0)

np = neopixel.NeoPixel(machine.Pin(14), 8)

np[0] = (0,0,0) # Red
np[1] = (0,0,0) #Yellow
np[2] = (0,0,0)   #Green

np.write()


def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp


while True:
    time.sleep(0.5)
    data = i2c.readfrom_mem(address, temp_reg, 2)
    print(temp_c(data))
    if temp_c(data) <= 28:
        np[0] = (0, 0, 0)  # Red
        np[1] = (0, 0, 0)  # Yellow
        np[2] = (255, 0, 0)  # Green
    elif 28 < temp_c(data) < 30:
        np[0] = (0, 0, 0)  # Red
        np[1] = (255, 255, 0)  # Yellow
        np[2] = (0, 0, 0)  # Green
    elif temp_c(data) >= 30:
        np[0] = (0, 255, 0)  # Red
        np[1] = (0, 0, 0)  # Yellow
        np[2] = (0, 0, 0)  # Green
    np.write()