import machine
import time
pinred = machine.Pin(12, machine.Pin.OUT)
pinyellow = machine.Pin(27, machine.Pin.OUT)
pingreen = machine.Pin(33, machine.Pin.OUT)
button = machine.Pin(15, machine.Pin.IN)


buttoncounter = 0
pingreen.value(1)
buttonstate = 1


while True:
    if buttonstate == 0 and button.value() == 0:
        buttonstate = 1
    time.sleep(0.01)
    print(button.value())
    if button.value() == 1 and buttonstate == 1:
        buttonstate = 0
        if pingreen.value() == 1:
            pingreen.value(0)
            pinyellow.value(1)
        elif pinyellow.value() == 1:
            pinyellow.value(0)
            pinred.value(1)
        elif pinred.value() == 1:
            pinred.value(0)
            pingreen.value(1)


