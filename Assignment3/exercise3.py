import machine
import time

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
listsensor = i2c.scan()
address = listsensor[0]
temp_reg = 5
res_reg = 8
pinred = machine.Pin(12, machine.Pin.OUT)
pinyellow = machine.Pin(27, machine.Pin.OUT)
pingreen = machine.Pin(33, machine.Pin.OUT)



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
        pinred.value(0)
        pinyellow.value(0)
        pingreen.value(1)
    elif 28 < temp_c(data) < 30:
        pinred.value(0)
        pingreen.value(0)
        pinyellow.value(1)
    elif temp_c(data) >= 30:
        pinred.value(1)
        pinyellow.value(0)
        pingreen.value()
