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

ax = [0.0]
ay = [0.0]
az = [0.0]

vx = [0.0]
vy = [0.0]
vz = [0.0]

x = [0.0]
y = [0.0]
z = [0.0]

r = []
temp = []
pitch = []
roll = []
time = [0.0]
dt = 0.1

for line in values:
    temp.append(line.split(' '))

for i in temp:
    for j in range(len(i)):
        if i[j] == 'x:':
            ax.append(float(i[j+1]))
        elif i[j] == 'y:':
            ay.append(float(i[j+1]))
        elif i[j] == 'z:':
            az.append(float(i[j+1][:len(i[j+1])-3]))

for i in range(len(ax)):
    r.append([ax[i], ay[i], az[i]])
    time.append(time[i] + dt)    

time.pop()

for i in range(len(ax)):
    pitch.append(np.arctan2(ay[i], np.sqrt(ax[i]**2 + az[i]**2)) * 180 / np.pi)
    roll.append(np.arctan2(-ax[i], az[i]) * 180 / np.pi)

plt.plot(time, pitch, label='pitch')
plt.plot(time, roll, label='roll')
plt.legend()
plt.grid()
plt.show()

plt.plot(time, ax, label='ax')
plt.plot(time, ay, label='ay')
plt.plot(time, az, label='az')
plt.legend()
plt.grid()
plt.show()

for i in range(1, len(ax)):
    vx.append(vx[i-1] + ax[i]*dt)
    vy.append(vy[i-1] + ay[i]*dt)
    vz.append(vz[i-1] + az[i]*dt)

    x.append(x[i-1] + vx[i]*dt)
    y.append(y[i-1] + vy[i]*dt)
    z.append(z[i-1] + vz[i]*dt)

plt.plot(time, vx, label='vx')
plt.plot(time, vy, label='vy')
plt.plot(time, vz, label='vz')
plt.legend()
plt.grid()
plt.show()

plt.plot(time, x, label='x')
plt.plot(time, y, label='y')
plt.plot(time, z, label='z')
plt.legend()
plt.grid()
plt.show()