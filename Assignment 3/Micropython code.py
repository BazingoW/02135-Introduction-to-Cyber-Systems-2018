#blink code

pin = machine.Pin(12, machine.Pin.OUT)

for i in range(10):
    pin.value(1)
    time.sleep(0.5)
    pin.value(0)
    time.sleep(0.5)
