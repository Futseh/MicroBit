from microbit import *

for i in range(2**25):
    st = bin(i)
    num = []

    for n in range(len(str(st))):
        if n == 0 or n == 1:
            pass
        else:
            num.append(9 * int(st[n]))

    num.reverse()

    y = 0
    x = 0

    for k in range(len(num)):
        if k > 4:
            if k > 9:
                if k > 14:
                    if k > 19:
                        y = 4
                        x = k - 20
                        display.set_pixel(x, y, num[k])
                    else:
                        y = 3
                        x = k - 15
                        display.set_pixel(x, y, num[k])
                else:
                    y = 2
                    x = k - 10
                    display.set_pixel(x, y, num[k])
            else:
                y = 1
                x = k - 5
                display.set_pixel(x, y, num[k])
        else:
            y = 0
            x = k
            display.set_pixel(x, y, num[k])

    sleep(250)
    display.clear()
