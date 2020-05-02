'''
simulation.py
-------------------
Created by Will Rice

This python script will simulate the positioning system for niminal values, creating a
Latin Hypercube Sampling of the Expected performance.
'''

# Core Modules
import math
import random as rand
import numpy as np

# Dataframes
import pandas as pd

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

# Importing python scripts
import PositionFunctions as pf

def run_scenario(move,phi,r1,rErr,tfErr):
    """Calculates the error range/accuracy for given positioning values.

    Arguments:
        move {int} -- Relative distance moved between robots.
        phi {float} -- Relative angle moved between robots.
        r1 {int} -- Starting Seperation between robots.
        rErr {float} -- Movement error (%). 0.2 = 20%.
        tfErr {int} -- Time of flight distance error.

    Returns:
        float -- Size of error range
    """
    # Defining
    start_coord = [0,r1]
    end_coord = [0,0]

    # Redefining end point
    end_coord[0] = start_coord[0] + move*math.cos(phi)
    end_coord[1] = start_coord[1] + move*math.sin(phi)

    # Calculating Ending seperation
    r2 = math.sqrt(end_coord[0]**2 + end_coord[1]**2)

    # Calling scenario from PositionFunctions.py
    error = pf.errorrange(move, phi, r1, r2, rErr, 0, tfErr)
    return error

def quick_rand(variaboi, smp_num):
    """Quickly creates an array of random points.

    Arguments:
        variaboi {list: size 3} -- Variable nominal range in form; min, mode, max.
        smp_num {int} -- Number of random points to generate.

    Returns:
        numpy array
    """    
    return variaboi[0] + (variaboi[2]-variaboi[0])*np.random.random(smp_num)

# Defining ranges
move_dist = [1, 500, 1000]
phis = [-math.pi, 0, math.pi]
start_radius = [100, 1000, 3000]
radius_error = [0, 0.2, 0.4]
tferror = [0, 100, 200]

# Nominal scenario
nom = run_scenario(move_dist[1],phis[1],start_radius[1],radius_error[1],tferror[1])

# Create random samples
smp_num = 13000
rand_move = quick_rand(move_dist, smp_num)
rand_phis = quick_rand(phis, smp_num)
rand_stra = quick_rand(start_radius, smp_num)
rand_rade = quick_rand(radius_error, smp_num)
rand_tfer = quick_rand(tferror, smp_num)

# latin supersampling
results = []
for i in range(0,smp_num):
    result = run_scenario(rand_move[i],rand_phis[i],rand_stra[i],rand_rade[i],rand_tfer[i])

    results.append(result)

# Creat pandas dataframe
df = pd.DataFrame(list(zip(rand_move,rand_phis,rand_stra,rand_rade,rand_tfer,results)),
    columns=['Movement Distance (mm)','Movement angle (rad)','Starting Seperation (mm)','Movement error (%)','Time of flight error (mm)','Error size (rad)'])

# Convert movement error to %
df['Movement error (%)'] = df['Movement error (%)']*100

# Create radius 2, ultimately unused
df['x'] = 0 + df['Movement Distance (mm)']*np.cos(df['Movement angle (rad)'])
df['y'] = df['Starting Seperation (mm)'] + df['Movement Distance (mm)']*np.sin(df['Movement angle (rad)'])
df['Ending Seperation (mm)'] = np.sqrt(df['x']**2 + df['y']**2)

# Plotting
g = sns.PairGrid(
    df,
    y_vars=["Error size (rad)"],
    x_vars=['Movement Distance (mm)','Starting Seperation (mm)','Movement error (%)','Time of flight error (mm)']
    )

g.map(sns.scatterplot, color=".3", marker="x", alpha=0.1)
g.set(ylim=(0, 4), yticks=[0, math.pi, 2*math.pi], ylabel="Error range")

plt.show()