'''
GeneralFunctions.py
-------------------
Created by Will Rice

Replicates many positioning functions from the robot in Python for trouble shooting.
'''

# Importing Modules
import math

def ang_scale(theta):
    '''
    Scales angle between -pi and pi

    >>> ang_scale(10)
    -2.5663706143591725
    >>> ang_scale(-10)
    2.5663706143591725
    '''
    while True:
        if theta <= -math.pi:
            theta = theta + 2*math.pi
        elif theta > math.pi:
            theta = theta - 2*math.pi
        else:
            break

    return theta

def ang_diff(ang1, ang2):
    '''
    Returns shortest from ang1 to ang2
    
    >>> ang_diff(1,2)
    1.0
    '''
    
    # Ensuring angles in correct range
    ang1 = ang_scale(ang1)
    ang2 = ang_scale(ang2)

    # Calculate both directions
    diff1 = ang_scale(ang2 - ang1)
    diff2 = ang_scale(ang2 - ang1 + 2*math.pi)

    # Find smallest and return
    if abs(diff1) < abs(diff2):
        return diff1
    else:
        return diff2

def ang_offset(ang_list):
    '''
    Converts a list of angles, to a centre angle and aclk + clk rotations

    >>> ang_offset([0,1,2])
    [-1.0, 1, 1.0]
    '''
    ang_list[1] = ang_scale(ang_list[1])
    
    ang_list[0] = ang_diff(ang_list[1], ang_list[0])
    ang_list[2] = ang_diff(ang_list[1], ang_list[2])
    return ang_list

def polar_add(radiusA, angleA, radiusB, angleB):
    '''
    Returns addition of two polar coordinates
    To perform a subtraction multiply radiusB by -1
    '''
    
    # https://math.stackexchange.com/questions/1365622/adding-two-polar-vectors
    radius = round(math.sqrt(pow(radiusA,2)+pow(radiusB,2)+(2*radiusA*radiusB*math.cos(angleB-angleA))))
    angle = angleA + math.atan2(radiusB*math.sin(angleB-angleA),radiusA+(radiusB*math.cos(angleB-angleA)))
    
    return [radius, angle]

def ang_flatten(ang_list):
    '''
    Converts a list of relative angles to flat angles

    >>> ang_flatten([-1.0, 1, 1.0])
    [0.0, 1, 2.0]
    '''
    ang_list[0] = ang_list[1] + ang_list[0]
    ang_list[2] = ang_list[1] + ang_list[2]
    return ang_list

def ang_overlap(list1, list2):
    '''
    Find overlap between two lists of angles.

    Parameters
    ----------
    list1
        Length 3 list of order;
            offset1, mode, offset2
    list2
        Length 3 list of order;
            offset1, mode, offset2

        All lists must have offset1 aclk to mode and offset2 clk to mode

    Returns
    -------
    ret_list
        Length 3 list of order;
            offset1, mode, offset2

    #>>> ang_overlap([0,-5,-1], [-2,-2.5,-3])
    []
    #>>> ang_overlap([0,-5,-1], [-0.7,-1,-2])
    [[-0.7, -1]]
    #>>> ang_overlap([0,-5,-1], [-0.3,-0.5,-0.7])
    [[-0.3, -0.7]]
    #>>> ang_overlap([0,-5,-1], [-2,-3,-0.5])
    [[0, -0.5]]
    '''

    # Scaled from pi <= ang < -pi
    A_aclk = ang_scale(list1[0])
    A_mode = ang_scale(list1[1])
    A_clk = ang_scale(list1[2])

    B_aclk = ang_scale(list2[0])
    B_mode = ang_scale(list2[1])
    B_clk = ang_scale(list2[2])

    # If A_clk is anticlockwise
    if A_aclk < A_clk:
        A_clk -= 2*math.pi
    # If B_aclk is anticlockwise
    if A_aclk < B_aclk:
        B_aclk -= 2*math.pi
    # If B_clk is anticlockwise
    if A_aclk < B_clk:
        B_clk -= 2*math.pi

    # If the next angle clockwise is A_clk, no ovelap
    pizza = []

    #       A         A    B       B
    #       ｜        ｜   ｜      ｜
    if A_aclk-A_clk < A_aclk-B_aclk and A_aclk-A_clk < A_aclk-B_clk:
        return pizza

    #       A    B    A    B
    #       ｜   ｜###｜   ｜
    elif A_aclk - A_clk >= A_aclk-B_aclk and A_aclk-A_clk < A_aclk-B_clk:
        pizza.append([B_aclk,None,A_clk])

    #       A  B   B  A
    #       ｜ ｜##｜ ｜
    elif A_aclk-B_clk >= A_aclk-B_aclk and A_aclk-B_clk < A_aclk-A_clk:
        pizza.append([B_aclk,None,B_clk])

    #       A  B      A    B
    #       ｜#｜     ｜   ｜
    elif A_aclk-B_clk < A_clk-B_aclk and A_aclk-A_clk < A_aclk-B_aclk:
        pizza.append([A_aclk,None,B_clk])

    #       A  B   B  A
    #       ｜#｜  ｜#｜
    else:
        pizza.append([A_aclk,None,B_clk])
        pizza.append([B_aclk,None,A_clk])

    # Looping through 1 or 2 solutions
    for n in range(0,len(pizza)):

        # Find the middle value
        lb = pizza[n][0]
        ub = pizza[n][2]

        if (lb + A_mode - B_mode - ub) != 0:
            pizza[n][1] = (lb*A_mode - B_mode*ub)/(lb + A_mode - B_mode - ub)
        else:
            pizza[n][1] = ((lb + ub)/2)

    return pizza

if __name__ == '__main__':

    # Run doctest
    import doctest
    doctest.testmod()
