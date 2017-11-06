from microbit import *

hrs = 18
mins = 50
sec = 50
hours = []
minutes = []
seconds = []

b = 9

def one(x):
    zero(x)
    display.set_pixel(x, 3, b),        

def two(x):
    zero(x)
    display.set_pixel(x, 2, b),

def three(x):
    zero(x)
    display.set_pixel(x, 3, b)
    display.set_pixel(x, 2, b),   

def four(x):
    zero(x)
    display.set_pixel(x, 1, b),

def five(x):
    zero(x)
    display.set_pixel(x, 3, b)
    display.set_pixel(x, 1, b),

def six(x):
    zero(x)
    display.set_pixel(x, 2, b)
    display.set_pixel(x, 1, b),

def seven(x):
    zero(x)
    display.set_pixel(x, 1, b)
    display.set_pixel(x, 2, b)
    display.set_pixel(x, 3, b),

def eight(x):
    zero(x)
    display.set_pixel(x, 0, b),

def nine(x):
    zero(x)
    display.set_pixel(x, 0, b)
    display.set_pixel(x, 3, b),    

def zero(x):
    for i in range(0,4):
        display.set_pixel(x, i, 0)

def fadesecs(x):
    display.set_pixel(2, 2, x)
    display.set_pixel(2, 1, x)

def background(x,y):
    if display.get_pixel(x, y) < 1: 
        display.set_pixel(x, y, 1)  

def backgrounds():
    for i in range(4):              
        background(0, i)
        background(1, i)
        background(3, i)
        background(4, i)
    
def printtime():
    print(str(hours)+":"+str(minutes)+":"+str(seconds))

binaries = [one, two, three, four, five, six, seven, eight, nine, zero]

def displaybinaries():
    global mins 
    global hrs
    global minutes
    global hours
    
    if mins<10:
        binaries[mins-1](4)     
        zero(3)                 
        backgrounds()            
    elif mins > 9:
        minutes = [int(i) for i in str(mins)]   
        binaries[minutes[0]-1](3)                
        binaries[minutes[1]-1](4)               
        backgrounds()
        
    if hrs<10:
        binaries[hrs-1](1)
        zero(0)
        backgrounds()
    elif hrs > 9:
        hours = [int(i) for i in str(hrs)]
        binaries[hours[0]-1](0)
        binaries[hours[1]-1](1)
        backgrounds()

def sleepbutton(x):
    global sec
    global hrs
    global mins
    
    if button_a.was_pressed():
        if hrs < 24:
            hrs += 1
        else:
            hrs = 0
            
        displaybinaries()
        print(hrs)
        
    if button_b.was_pressed():
        if mins < 60:
            mins += 1
            sec = 0
        else:
            mins = 0
            sec = 0
        
        displaybinaries()
        print(mins)
    sleep(x)
 
while True:
    for i in range(0,5):    
        sleepbutton(99) 
        
    fadesecs(1)       
    
    for i in range(0,5):    
        sleepbutton(98) 
        
    fadesecs(4)             
    sec += 1
    
    if sec % 60 == 0:       
        mins += 1
        
        if mins % 60 == 0:
            hrs += 1
            mins = 0
            
            if hrs % 24 == 0:
                hrs = 0
                
    seconds=str(sec)
    minutes=str(mins)
    hours=str(hrs)
    printtime()
    displaybinaries()