import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def format_data(df):
    # Create Heading
    df['Heading'] = df.apply(lambda row: math.atan2(row.Y_Axis,row.X_Axis) if math.atan2(row.Y_Axis,row.X_Axis) < 0 else math.atan2(row.Y_Axis,row.X_Axis) - 2*math.pi, axis=1)

    # Reformat
    df = df.iloc[10:131]
    df = df.reset_index(drop=True)

    # Find max and min
    df_len = len(df['X_Axis'].values.tolist())
    
    x_max = [max(df['X_Axis'])]*df_len
    x_min = [min(df['X_Axis'])]*df_len

    y_max = [max(df['Y_Axis'])]*df_len
    y_min = [min(df['Y_Axis'])]*df_len

    h_max = [max(df['Heading'])]*df_len
    h_min = [min(df['Heading'])]*df_len

    return df, x_max, x_min, y_max, y_min, h_max, h_min

def vary_plot(df, x_max, x_min, y_max, y_min, h_max, h_min, titl):
    # Defining
    fig, ax1 = plt.subplots(num='ggplot')

    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Magnetic Field')

    ax1.plot(df['X_Axis'], color='tab:red', label='X Axis')
    ax1.plot(df['Y_Axis'], color='tab:blue', label='Y Axis')

    ax1.plot(x_max, color='tab:red', linestyle='--')
    ax1.plot(x_min, color='tab:red', linestyle='--')

    ax1.plot(y_max, color='tab:blue', linestyle='--')
    ax1.plot(y_min, color='tab:blue', linestyle='--')

    plt.xlim(0,len(df['X_Axis'].values.tolist())-1)
    plt.ylim(-8000,8000)

    ax1.legend(loc=2)

    ax2 = ax1.twinx()

    color = 'tab:green'
    ax2.set_ylabel('Heading (Radians)', color=color)

    ax2.plot(df['Heading'], color=color, label='Heading')
    ax2.tick_params(axis='y', labelcolor=color)

    ax2.plot(h_max, color='tab:green', linestyle='--')
    ax2.plot(h_min, color='tab:green', linestyle='--')

    plt.ylim(-4,4)
    
    ax2.legend(loc=1)

    fig.tight_layout()
    plt.title(titl)

    # Saving
    name_str = titl+'.pdf'
    fig.savefig(name_str)


# Read data
static = pd.read_csv('StaticTest1.csv')
dynam = pd.read_csv('DynamicTest1.csv')

# format
static, s_x_max, s_x_min, s_y_max, s_y_min, s_h_max, s_h_min = format_data(static)
dynam, d_x_max, d_x_min, d_y_max, d_y_min, d_h_max, d_h_min = format_data(dynam)

# Plotting
vary_plot(static, s_x_max, s_x_min, s_y_max, s_y_min, s_h_max, s_h_min, 'Motor Off')
vary_plot(dynam, d_x_max, d_x_min, d_y_max, d_y_min, d_h_max, d_h_min, 'Motor On')

#plt.show()

# Returning Key stats
motoroff = '+/- '+str(round(abs(s_h_max[0]-s_h_min[0])/2,3))+' rads'
motoron  = '+/- '+str(round(abs(d_h_max[0]-d_h_min[0])/2,3))+' rads'

motoroffd = '+/- '+str(round(abs(s_h_max[0]-s_h_min[0])*90/math.pi,3))+' degrees'
motorond  = '+/- '+str(round(abs(d_h_max[0]-d_h_min[0])*90/math.pi,3))+' degrees'

print('Compass Accuracy motor off:')
print(motoroff)
print(motoroffd)
print('Compass Accuracy motor on:')
print(motoron)
print(motorond)