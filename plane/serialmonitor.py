import serial, time

port = '/dev/ttyACM0'
baud = 115200

s = serial.Serial(port)
s.baudrate = baud

file = open('data.dat', 'w')

try:
    while True:
        data = s.readline()
        data = data[:len(data)-2]
        file.write(str(data)[2:len(data)+2] + '\n')
        print(str(data)[2:len(data)+2])
except KeyboardInterrupt:
    file.close()