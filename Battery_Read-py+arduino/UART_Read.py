'''
UART_Read.py
------------
Created by Will Rice

Reads in from Arduino UART and ouputs to file.
'''

# Importing modules
import serial
from datetime import datetime
import matplotlib.pyplot as plt
import winsound

# Print available port
# python -m serial.tools.list_ports

# Filename
filename = 'discharge_test_2.csv'

# Defining port
ser = serial.Serial()
ser.port = 'COM6'
ser.timeout = 10
ser.open()
print(ser)

batterylevels = []
# Create plot
# draw the figure so the animations will work
#fig = plt.gcf()
#fig.show()
#fig.canvas.draw()

# Reading from port
while True:
    line = str(ser.readline())
    line = line.split("'")[1]
    line = line[:-4]
    if line == "Warning! Low Voltage":
        print(line)
        winsound.Beep(2500,1000)
        continue

    now = datetime.now()
    currtime = now.strftime("%H:%M:%S:%f")

    printstr = str(currtime)+","+str(line)
    print(printstr)
    with open(filename,'a') as fd:
        fd.write(printstr+"\n")

    #batterylevels.append(float(line))

    #plt.plot(batterylevels)
    #fig.canvas.draw()

plt.show()