'''
Plotting.py
-------------------
Created by Will Rice

Creates a fancy plot that shows how the positioning system operates.
'''

# Importing modules
import math
import sympy as syp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Global variables
xlimits = (-200, 500)
ylimits = (-200, 500)

def scenario1(ax):
    # To be plotted
    RobotAx = [0,0]
    RobotAy = [0,50]
    RobotBx = [400,250]
    RobotBy = [100,80]

    new_circle = plt.Circle((0, 50), math.sqrt(250**2 + 30**2),
                            color='r',
                            fill =False,
                            label='New distance')
    old_circle = plt.Circle((0, 0), math.sqrt(400**2 + 100**2),
                            color='b',
                            fill =False,
                            label='Old distance')

    # Plotting
    ax.set_title('Before and After Moving')

    ax.add_artist(old_circle)
    ax.add_artist(new_circle)
    
    ax.plot(RobotAx, RobotAy, '-xb', label='Robot A')
    ax.plot(RobotBx, RobotBy, '--or', label='Robot B')

    # Setting axis
    ax.set_xlim(xlimits)
    ax.set_ylim(ylimits)

    # Add legend
    ax.legend()

def scenario2(ax):
    # To be plotted
    RobotAx = [0]
    RobotAy = [0]
    RobotBx = [400,250]
    RobotBy = [100,30]
    Relmovex = [0,-150]
    Relmovey = [0,-70]

    new_circle = plt.Circle((0, 0), math.sqrt(250**2 + 30**2),
                            color='r',
                            fill =False)
    old_circle = plt.Circle((-150, -70), math.sqrt(400**2 + 100**2),
                            color='b',
                            fill =False)

    # Plotting
    ax.set_title('Relative around A')

    ax.add_artist(old_circle)
    ax.add_artist(new_circle)
    
    ax.plot(Relmovex, Relmovey, '--xg', label='Relative Movement')
    ax.plot(RobotAx, RobotAy, '-xb', label='Robot A')
    ax.plot(RobotBx, RobotBy, '--or', label='Robot B')

    # Add legend
    ax.legend()

def scenario3(ax):
    # To be plotted
    RobotAx = [0]
    RobotAy = [0]
    RobotBx = [400,250]
    RobotBy = [100,30]
    Relmovex = [0,-150]
    Relmovey = [0,-70]

    new_circle = plt.Circle((0, 0), math.sqrt(250**2 + 30**2),
                            color='r',
                            fill =False)
    old_circle = plt.Circle((-150, -70), math.sqrt(400**2 + 100**2),
                            color='b',
                            fill =False)

    interAx = [0, 250]
    interAy = [0, 30]

    interBx = [0, 183]
    interBy = [0, 172]

    # Plotting
    ax.set_title('Possible Angles')
  
    ax.add_artist(old_circle)
    ax.add_artist(new_circle)
    
    ax.plot(Relmovex, Relmovey, '--xg', label='Relative Movement')
    ax.plot(RobotAx, RobotAy, '-xb', label='Robot A')
    ax.plot(RobotBx, RobotBy, '--or', label='Robot B')
    ax.plot(interAx, interAy, ':', label='Possible Location 1')
    ax.plot(interBx, interBy, ':', label='Possible Location 2')

    # Add legend
    ax.legend()

def scenario4(ax):
    # To be plotted
    RobotAx = [0]
    RobotAy = [0]
    RobotBx = [400,250]
    RobotBy = [100,30]
    Relmovex = [0,-150]
    Relmovey = [0,-70]

    new_circle = plt.Circle((0, 0), math.sqrt(250**2 + 30**2),
                            color='r',
                            fill =False)
    old_circle = plt.Circle((-150, -70), math.sqrt(400**2 + 100**2),
                            color='b',
                            fill =False)

    interAx = [0, 250]
    interAy = [0, 30]

    interBx = [0, 183]
    interBy = [0, 172]

    # 18.069321496584795
    # 4.978019420067535
    # -22.860294088946215
    
    # 78.0212130681621
    # 43.19101354357104
    # 25.16871620973132
    errorA = mpatches.Arc((0,0), 0.9*math.sqrt(250**2 + 30**2), 0.9*math.sqrt(250**2 + 30**2), angle=0, theta1=-22, theta2=18, ls='-.', color='black')
    errorB = mpatches.Arc((0,0), 0.9*math.sqrt(250**2 + 30**2), 0.9*math.sqrt(250**2 + 30**2), angle=0, theta1=25, theta2=78, ls='-.', color='black')

    lineAx = [0, 240]
    lineAy = [0, 78]

    lineBx = [0, 233]
    lineBy = [0, -94]

    lineCx = [0, 52]
    lineCy = [0, 246]

    lineDx = [0, 228]
    lineDy = [0, 106]

    # Arc lines**

    # Plotting
    ax.set_title('Possible Angles with Error')
  
    ax.add_artist(old_circle)
    ax.add_artist(new_circle)

    ax.add_artist(errorA)
    ax.add_artist(errorB)

    ax.plot(lineAx, lineAy, '-.', color='black', label='Location with Error')
    ax.plot(lineBx, lineBy, '-.', color='black')
    ax.plot(lineCx, lineCy, '-.', color='black')
    ax.plot(lineDx, lineDy, '-.', color='black')
    
    ax.plot(Relmovex, Relmovey, '--xg', label='Relative Movement')
    ax.plot(RobotAx, RobotAy, '-xb', label='Robot A')
    ax.plot(RobotBx, RobotBy, '--or', label='Robot B')
    ax.plot(interAx, interAy, ':', label='Possible Location 1')
    ax.plot(interBx, interBy, ':', label='Possible Location 2')

    # Add legend
    ax.legend()
    
if __name__ == '__main__':
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, gridspec_kw={'hspace': 0, 'wspace': 0})
    scenario1(axs[0,0])
    scenario2(axs[0,1])
    scenario3(axs[1,0])
    scenario4(axs[1,1])

    # Hide x labels and tick labels for all but bottom plot.
    for ax in axs.flat:
        ax.label_outer()

    # stuff
    fig.set_size_inches(10, 8)

    plt.show()
    #plt.savefig('PositioningSystem.png', bbox_inches='tight')