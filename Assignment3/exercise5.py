import machine
import neopixel

#Neopixel colors (G,R,B)
# Red (0,255,0)
# Yellow (255,255,0)
#Green (255,0,0)

np = neopixel.NeoPixel(machine.Pin(14), 8)

np[0] = (0,0,0) # Red
np[1] = (0,0,0) #Yellow
np[2] = (0,0,0)   #Green

np.write()

#CS - A1 pin 25

spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0)
cs = machine.Pin(25, machine.Pin.OUT)
cs.value(1)
spi.write(b'\b1000')
cs.value(0)
data = spi.read(4)
cs.value(1)
print(data)