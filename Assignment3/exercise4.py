import machine
import neopixel

#Neopixel colors (G,R,B)
# Red (0,255,0)
# Yellow (255,255,0)
#Green (255,0,0)

np = neopixel.NeoPixel(machine.Pin(14), 8)

"""
np[0] = (0,255,0) # Red
np[1] = (255,255,0) #Yellow
np[2] = (255,0,0)   #Green
"""

np[0] = (0,0,0) # Red
np[1] = (0,0,0) #Yellow
np[2] = (0,0,0)   #Green

np.write()