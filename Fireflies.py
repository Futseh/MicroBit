from microbit import *
import radio
import random

flash = Image("99999:99999:99999:99999:99999")

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('flash')
    
    incoming = radio.receive()
    
    if incoming == 'flash':
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        sleep(500)
        radio.send('flash')
        sleep(100)
        display.clear()