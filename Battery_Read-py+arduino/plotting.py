'''
plotting.py
------------------
Created by Will Rice

Created for Andrew Guest, to interpret battery data into a graph.
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
        first_val = (first_val*(steps-1)+row[1])/steps
        out.append(first_val)
    return out

# Read in data
df = pd.read_csv('discharge_test_2.csv', header=None)

# Rolling Averages
rolling10 = rollingaverage(df, 10)
rolling20 = rollingaverage(df, 20)
rolling30 = rollingaverage(df, 30)
rolling50 = rollingaverage(df, 50)

# Plotting
plt.plot(df[1],'x',label='Recorded')
plt.plot(rolling10,label='10 Point Moving Average')
plt.plot(rolling20,label='20 Point Moving Average')
plt.plot(rolling50,label='50 Point Moving Average')

# Formatting
plt.xlim(0)
plt.ylim([3, 4.5])
plt.title('Battery Discharge')
plt.xlabel('Time (s)')
plt.ylabel('Voltage across battery (V)')
plt.legend()

plt.show()
#plt.savefig('battery_discharge.pdf')