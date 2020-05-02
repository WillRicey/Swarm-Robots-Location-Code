'''
UART_Reader.py
--------------
Created by Will Rice

Reads from Arduino port and outputs to csv with timestamp
'''

# Importing Modules
import serial
from datetime import datetime

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

# Reading from port
while True:
    # Reading and formatting
    line = str(ser.readline())
    line = line.split("'")[1]
    line = line[:-4]

    # Getting time
    now = datetime.now()
    currtime = now.strftime("%H:%M:%S:%f")

    # Output
    printstr = str(currtime)+","+str(line)
    print(printstr)
    with open(filename,'a') as fd:
        fd.write(printstr+"\n")