
import random
from microbit import *

rock = Image("00900:09990:99999:09990:00900")
paper = Image("99999:99999:99999:99999:99999")
scissors = Image("99099:99099:00900:09090:90009")

choices = [rock, paper, scissors]

while True:
    if accelerometer.is_gesture("shake"):
        im = random.choice(choices)
        display.show(im)
    else:
        pass