import radio
from microbit import *

g = 9.81

radio.on()

for i in range(2000):
    x = accelerometer.get_x() * (g / 1000)
    y = accelerometer.get_y() * (g / 1000)
    z = accelerometer.get_z() * (g / 1000)
    
    radio.send('x: %.2f y: %.2f z: %.2f' % (x, y, z))
    
    sleep(100)