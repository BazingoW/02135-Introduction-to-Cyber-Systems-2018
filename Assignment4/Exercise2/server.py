import machine #imports machine library
import network #imports network library
import socket #imports socket library
import json

ap = network.WLAN (network.AP_IF) #Sets up an access point that allows other WiFi clients to connect to it
ap.active (True) #Sets the access point to active
ap.config (essid = 'ESP32-WIFI-NAMEa') #Sets up the name of the access point to any given string (essid)
ap.config (authmode = 3, password = 'WiFi-password') #Setting the access point encryption type to WPA2-PSK and setting the access point password to a given string


#Setting up pins as a variable that fetches all the inputs (the value read from the pin/whether it is on or off) of the listed pins, and saving them in a list
pins = [machine.Pin(i, machine.Pin.IN) for i in ([15])]

#html description

#setting up the variable html as a document with type .html
#html code for an html file. The <html> tag shows that the file is an html file
#The <head> tag demarcates the head of the page
#The <title> tag is for for formatting the text in the head as a title
#The <body> tag is to demarcate the body of the file from the head
#Inside the body, the <h1> tag demarcates a header inside the body
#Creating a table with the name of the Pins in one column and the value of the corresponding pin in an adjacent column
#All tags are closed with the corresponding </> tags
html = """<!DOCTYPE html> 
<html>
    <head> <title>ESP32 Pins</title> </head>
    <body> <h1>ESP32 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

#Getting the address information in IPV4 format, with port
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]


s = socket.socket() #Setting up a socket with default parameters.
s.bind(addr) #"plugging in" the address to the socekt that was set up
s.listen(1) #Waiting to receive data to to the socket. The 1 is the backlog. The backlog is the maximum amount of clients that can try to connect at any given moment.

print('listening on', addr) #Prints out the address on which the socket is listening.


#While true: means that it's always listening
#S is the welcome socket that just accepts connections
#For each new client that connects, a new client socket is connected and a new ip address for the client is created.
#Prits out the IP address of the client that just connects
#Creates a new file object associated with the socket of type "read, write, binary" . The zero is the buffering. Micropython doesn't support buffered streams so this value is ignored. This file is to receive the TCP requests
#Create a while loop to read through the lines in the client file
#Sets the value of the variable "line" to the string that is read from the file containing TCP requests
# reads the stream of TCP requests. If there are no requests or the requests read "b'\r\n" (which is the break) the while loop breaks
#Sets the variable "rows" to a list of Pin names and their values read from each pin in pins, above
#Response is the variable created by joining the list of rows into the html file specfied above
#Cl send sends the response file to the client
#The socket is closed after the html file is sent to the client

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
listsensor = i2c.scan()
address = listsensor[0]
temp_reg = 5
res_reg = 8

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp



while True:
    data = i2c.readfrom_mem(address, temp_reg, 2)
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if "/pins" in line:

        print(line)
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % ("Button", p.value()) for p in pins]
    rowstemp = rows.append('<tr><td>%s</td><td>%f</td></tr>' % ("Temperature", temp_c(data)))
    response = html % '\n'.join(rows)
    cl.send(response)

    cl.close()


