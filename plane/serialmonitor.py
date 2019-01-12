import serial, time
import numpy as np
import matplotlib.pyplot as plt
"""
port = '/dev/ttyACM0'
baud = 115200

s = serial.Serial(port)
s.baudrate = baud

file = open('data.dat', 'w')

endFile = 'Type "help()" for more information.\r'

strData = ''

while strData != endFile:
    data = s.readline()
    #data = data[:len(data)-2]
    file.write(str(data)[2:len(data)+2] + '\n')
    print(str(data))
    strData = str(data)

file.close()
"""
with open('data.dat', 'r') as f:
    values = f.readlines()

g = -9.73

x = [g, 0.0, 0.0]
y = [0.0, g, 0.0]
z = [0.0, 0.0, g]

xt = []
yt = []
zt = []
r = []
temp = []

for line in values:
    temp.append(line.split(' '))

for i in temp:
    for j in range(len(i)):
        if i[j] == 'x:':
            xt.append(float(i[j+1]))
        elif i[j] == 'y:':
            yt.append(float(i[j+1]))
        elif i[j] == 'z:':
            zt.append(float(i[j+1][:len(i[j+1])-3]))

for i in range(len(xt)):
    r.append([xt[i], yt[i], zt[i]])

for i in r:
    print(i)