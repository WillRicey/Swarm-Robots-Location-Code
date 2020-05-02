import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name = '10HzOS128'

# Read data
data = pd.read_csv(name+'.csv')

# New frame
pdata = data

pdata = pdata.iloc[25:]
pdata = pdata.reset_index(drop=True)

print(pdata)

# Getting Upper and Lower
x_max = [max(pdata['X_Axis'])]*len(pdata['X_Axis'].values.tolist())
x_min = [min(pdata['X_Axis'])]*len(pdata['X_Axis'].values.tolist())

y_max = [max(pdata['Y_Axis'])]*len(pdata['X_Axis'].values.tolist())
y_min = [min(pdata['Y_Axis'])]*len(pdata['X_Axis'].values.tolist())

h_max = [max(pdata['Heading'])]*len(pdata['X_Axis'].values.tolist())
h_min = [min(pdata['Heading'])]*len(pdata['X_Axis'].values.tolist())

print(h_max[0]-h_min[0])


# Plotting
fig, ax1 = plt.subplots()

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Magnetic Field')

ax1.plot(pdata['X_Axis'], marker='o', color='tab:red', label='X Axis')
ax1.plot(pdata['Y_Axis'], marker='x', color='tab:blue', label='Y Axis')

ax1.plot(x_max, color='tab:red', linestyle='--')
ax1.plot(x_min, color='tab:red', linestyle='--')

ax1.plot(y_max, color='tab:blue', linestyle='--')
ax1.plot(y_min, color='tab:blue', linestyle='--')

plt.xlim(0,len(pdata['X_Axis'].values.tolist())-1)
plt.ylim(-2000,2000)

ax1.legend(loc=2)

ax2 = ax1.twinx()

ax2.set_ylabel('Heading (Radians)', color='tab:green')

ax2.plot(pdata['Heading'], marker='^', color='tab:green', label='Heading')
ax2.tick_params(axis='y', labelcolor='tab:green')

ax2.plot(h_max, color='tab:green', linestyle='--')
ax2.plot(h_min, color='tab:green', linestyle='--')

plt.ylim(0,3)

ax2.legend(loc=1)

fig.tight_layout()

plt.title(name)

plt.show()
