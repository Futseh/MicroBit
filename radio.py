from microbit import *
from radio import *

radio.on()
radio.config(channel=19, power=7)

my_message = "Be nice to yu turkeys dis christmas, Cos' turkeys just wanna hav fun, Turkeys are cool, turkeys are wicked, An every turkey has a Mum."

# Event loop.
while True:
        radio.send(my_message)
        incoming = radio.receive()
        
        if incoming is not None:
            display.show(incoming)
            print(incoming)
        
        sleep(500)