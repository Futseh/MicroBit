from microbit import *

for y in range(5):
    for x in range(5):
        sleep(1000)
        if x != 0:
            if display.get_pixel(x-1, y) != 0:
                display.set_pixel(x-1, y, 0)
                display.set_pixel(x, y, 9)
            else:
                display.set_pixel(x, y, 9)
        else:
            if y != 0:
                if display.get_pixel(4, y-1) != 0:
                    display.set_pixel(4, y-1, 0)
                    display.set_pixel(x, y, 9)
                else:
                    display.set_pixel(x, y, 9)
            else:
                display.set_pixel(x, y, 9)