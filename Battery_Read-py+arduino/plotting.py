import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('discharge_test_2.csv', header=None)

rolling10 = []
boi = 4.1

for index, row in df.iterrows():
    boi = (boi*9 + row[1])/10
    rolling10.append(boi)

rolling20 = []
boi = 4.1

for index, row in df.iterrows():
    boi = (boi*19 + row[1])/20
    rolling20.append(boi)

rolling50 = []
boi = 4.1

for index, row in df.iterrows():
    boi = (boi*49 + row[1])/50
    rolling50.append(boi)

plt.plot(df[1],'x',label='Recorded')
plt.plot(rolling10,label='10 Point Moving Average')
plt.plot(rolling20,label='20 Point Moving Average')
plt.plot(rolling50,label='50 Point Moving Average')

plt.xlim(0)
plt.ylim([3, 4.5])

plt.title('Battery Discharge')
plt.xlabel('Time (s)')
plt.ylabel('Voltage across battery (V)')

plt.legend()

plt.savefig('battery_discharge.pdf')
