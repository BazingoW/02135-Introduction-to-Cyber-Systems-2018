import machine
import time

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
listsensor = i2c.scan()
address = listsensor[0]
temp_reg = 5
res_reg = 8

data = i2c.readfrom_mem(address, temp_reg, 2)
print(data)
print(address)


def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp


temp_c(data)

print(temp_c(data))

i2c.writeto_mem(address, res_reg, b'\x00')

while True:
    time.sleep(0.5)
    data = i2c.readfrom_mem(address, temp_reg, 2)
    print(temp_c(data))