import radio
from microbit import *

g = 9.81

radio.on()

while True:
    message = radio.receive()
    print(message)
    sleep(100)