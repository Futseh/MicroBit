import radio
from microbit import *

g = 9.81

radio.on()

for i in range(2000):
    message = radio.receive()
    print(message)
    sleep(100)