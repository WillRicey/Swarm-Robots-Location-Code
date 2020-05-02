'''
PositionFunctions.py
--------------------
Created by Will Rice

Replicates many positioning functions from the robot in Python for trouble shooting.
'''

# Importing Modules
import math

def relative(relAngle, angle):
    '''
    Returns the relative displacement from the angle.

    >>> relative(1,2)
    1
    >>> relative(8,9)
    1
    '''

    maxAngle = relAngle + math.pi
    minAngle = relAngle - math.pi

    while True:
        if angle < minAngle:
            angle += 2*math.pi
        elif angle > maxAngle:
            angle -= 2*math.pi
        else:
            break

    angle = angle - relAngle

    return angle

def ricecalc(rMove, phiMove, r1, r2):
    '''
    Calculate the angle of the other robot.

    Parameters
    ----------
    rMove
        Radius of polar coordinate of relative movement.
    phiMove
        Angle in radians of relative movement.
    r1
        Old transmission distance.
    r2
        Most recent transmission distance.

    Returns
    -------
    [theta1, theta2]
        Possible angles of other robot.

    >>> ricecalc(500, 1, 2000, 1700)
    [3.124470460808594, -1.1001900280453456]
    '''

    # Defining
    m = rMove
    xrel = int(round(rMove*math.cos(phiMove),0))
    yrel = int(round(rMove*math.sin(phiMove),0))
    gam = -pow(r1,2)+pow(r2,2)+pow(m,2)

    # Ensuring root returns a real number (sometime close to zero due to rounding)
    insideroot = -( pow(r1-r2,2)-pow(m,2) )*( pow(r1+r2,2)-pow(m,2) )
    if insideroot < 0:
        root = 0
    else:
        root = math.sqrt(insideroot).real
    
    # Calculating values for y/x
    y1 = +(xrel*(xrel*root + yrel*gam))
    y2 = -(xrel*(xrel*root - yrel*gam))
    x1 = -yrel*(xrel*root - yrel*gam) + pow(m,2)*gam
    x2 = +yrel*(xrel*root - yrel*gam) + pow(m,2)*gam

    # Calculating angles
    theta1 = math.atan2(y1, x1)
    theta2 = math.atan2(y2, x2)

    # Returning
    return [theta1,theta2]

def errorcalc(rMove, phiMove, r1, r2, rErr, phiErr, tfErr):
    '''
    Calculates the min and max error given values for error.
    
    Parameters
    ----------
    rMove
        Radius of polar coordinate of relative movement.
    phiMove
        Angle in radians of relative movement.
    r1
        Old transmission distance.
    r2
        Most recent transmission distance.
    rErr
        Percent error (0.02 for 2%).
    phiErr
        Angle error in radians.
    tfErr
        Transmission error in mm.

    Returns
    -------
    [max_angle, min_angle]
        Each composed of a length 2 list

    >>> errorcalc(500, 1, 2000, 1700, 0.2, 0, 100)
    [[2.958994035065673, -0.834251461336172], [-2.8816618338040927, -2.146489334641508]]
    '''

    # Max rMove with error
    max_move = (rMove*(1+rErr))+tfErr
    min_move = (rMove*(1-rErr))-tfErr

    # r2-r1 < move < r2 + r1
    if max_move < r2 - r1:
        max_move = r2 - r1
    elif max_move > r2 + r1:
        max_move = r2 + r1

    if min_move < r2 - r1:
        min_move = r2 - r1
    elif min_move > r2 + r1:
        min_move = r2 + r1

    # Large error
    max_angle = ricecalc(max_move, phiMove, r1, r2)
    min_angle = ricecalc(min_move, phiMove, r1, r2)
    
    return [max_angle, min_angle]

def completecalc(rMove, phiMove, r1, r2, rErr, phiErr, tfErr):
    '''
    Calculates the min and max error and the middle result.
    
    Parameters
    ----------
    rMove
        Radius of polar coordinate of relative movement.
    phiMove
        Angle in radians of relative movement.
    r1
        Old transmission distance.
    r2
        Most recent transmission distance.
    rErr
        Percent error (0.02 for 2%).
    phiErr
        Angle error in radians.
    tfErr
        Transmission error in mm.

    Returns
    -------
    2x3 list
        Returns two lists with the format
            Offset
            Middle
            Offset

    >>> completecalc(500, 1, 2000, 1700, 0.2, 0, 100)
    [[-2.8816618338040927, 3.124470460808594, 2.958994035065673], [-0.834251461336172, -1.1001900280453456, -2.146489334641508]]
    '''
    result = ricecalc(rMove, phiMove, r1, r2)
    errorresult = errorcalc(rMove, phiMove, r1, r2, rErr, phiErr, tfErr)

    # Reformatting as min, mid, max
    # min is anticlockwise from mid
    # max is clockwise from mid
    if abs(relative(result[0], errorresult[0][0])) < abs(relative(result[0], errorresult[1][0])):
        if relative(result[0], errorresult[0][0]) < 0:
            dirA = [errorresult[1][0], result[0], errorresult[0][0]]
        else:
            dirA = [errorresult[0][0], result[0], errorresult[1][0]]
    else:
        if relative(result[0], errorresult[1][0]) > 0:
            dirA = [errorresult[1][0], result[0], errorresult[0][0]]
        else:
            dirA = [errorresult[0][0], result[0], errorresult[1][0]]

    if abs(relative(result[1], errorresult[0][1])) < abs(relative(result[1], errorresult[1][1])):
        if relative(result[1], errorresult[0][1]) < 0:
            dirB = [errorresult[1][1], result[1], errorresult[0][1]]
        else:
            dirB = [errorresult[0][1], result[1], errorresult[1][1]]
    else:
        if relative(result[1], errorresult[1][1]) > 0:
            dirB = [errorresult[1][1], result[1], errorresult[0][1]]
        else:
            dirB = [errorresult[0][1], result[1], errorresult[1][1]]

    return [dirA, dirB]

def rangefinder(minp, maxp):
    if minp > maxp:
        return minp-maxp
    else:
        return (minp+(2*math.pi))-maxp

def errorrange(rMove, phiMove, r1, r2, rErr, phiErr, tfErr):
    complete = completecalc(rMove, phiMove, r1, r2, rErr, phiErr, tfErr)
    A = rangefinder(complete[0][0],complete[0][2])
    B = rangefinder(complete[1][0],complete[1][2])

    return max(A,B)
    

if __name__ == '__main__':

    # Run doctest
    import doctest
    doctest.testmod()

    print(errorrange(500, 1, 2000, 1700, 0.2, 0, 100))
