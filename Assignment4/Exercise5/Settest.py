import sys

while True:
    i = input()
    if "/setnp" in input:
        stringlist = input.split("/")
        number = stringlist[1]
        green = stringlist[2]
        red = stringlist[3]
        blue = stringlist[4]
        print(green + "," + blue)

    elif "/set" in input:
        stringlist = input.split('/')
        pin = stringlist[1]
        print(pin)


        value = stinglist[2]
        pin.value(value)




        np[number] = (green, red, blue)
        np.write()