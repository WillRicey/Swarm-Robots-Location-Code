'''
plotting_charge.py
------------------
Created by Will Rice

Created for Andrew Guest, to interpret battery charge data into a graph.
'''

# Import Modules
import matplotlib.pyplot as plt
import pandas as pd

# Define Functions
def rollingaverage(dataframe, steps, first_val=3.56):
    """Creates rolling average.

    Arguments:
        dataframe {pandas dataframe} -- 2 columns, time and value
        steps {int} -- Nume of steps to average to.

    Keyword Arguments:
        first_val {float} -- (default: {3.56})

    Returns:
        list -- average values
    """    
    out = []
    for index, row in dataframe.iterrows():
        average = (average*(steps-1)+row[1])/steps
        out.append(average)
    return out

# Read in data
df = pd.read_csv('charge_test.csv', header=None)

# Remove bad values
df = df[df[1]>3.4]

# Rolling Averages
rolling10 = rollingaverage(df, 10)
rolling20 = rollingaverage(df, 20)
rolling30 = rollingaverage(df, 30)
rolling50 = rollingaverage(df, 50)

# Plotting data
plt.plot(df[1],'x',label='Recorded')
plt.plot(rolling10,label='10 Point Moving Average')
plt.plot(rolling20,label='20 Point Moving Average')
plt.plot(rolling50,label='50 Point Moving Average')

# Formatting plot
plt.xlim(0)
plt.ylim([3.4, 4])
plt.title('Battery Charge')
plt.xlabel('Time (s)')
plt.ylabel('Voltage across battery (V)')
plt.legend()

plt.show()

#plt.savefig('battery_charge.pdf')