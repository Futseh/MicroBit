# Add your Python code here. E.g.
from microbit import *
import radio
import random

flash = [Image().invert() * (i / 9) for i in range(9, -1, -1)]

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('flash')
    
    incoming = radio.receive()
    
    if incoming == 'flash':
        sleep(radnom.randint(50, 350))
        display.show(flash, delay=100, wait=false)
        
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')