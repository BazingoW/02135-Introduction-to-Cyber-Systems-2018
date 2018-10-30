#blink code

#Exercise 1

import machine
import time
import machine
import time
pin = machine.Pin(12, machine.Pin.OUT)
button = machine.Pin(15, machine.Pin.IN)


while True:
    time.sleep(0.01)
    if button.value() == 1:
        pin.value(1)
        time.sleep(0.5)
        pin.value(0)
        time.sleep(0.5)









