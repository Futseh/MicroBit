from microbit import *

counter = 9

zero = Image("09990:90009:90009:90009:09990")
one = Image("00900:09900:00900:00900:09990")
two = Image("99990:00009:09990:90000:99999")
three = Image("99999:00009:00090:90009:09990")
four = Image("00990:09090:90090:99999:00090")
five = Image("99999:90000:99990:00009:99990")
six = Image("00090:00900:09990:90009:09990")
seven = Image("99999:00090:00900:09000:90000")
eight = Image("09990:90009:09990:90009:09990")
nine = Image("09990:90009:09990:00900:09000")

num = [zero, one, two, three, four, five, six, seven, eight, nine]

while (True):
    
    display.show(num[counter])
    
    if button_a.is_pressed():
        sleep(250)
        
        if counter == 9:
            counter = 0
        else:
            counter += 1
    
    if button_b.is_pressed():
        sleep(250)
        
        if counter == 0:
            counter = 9
        else:
            counter -= 1
    
    if counter < 0:
        break