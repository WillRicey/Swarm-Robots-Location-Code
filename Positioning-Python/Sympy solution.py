import math
import sympy as syp

def sypSolution():

    x = syp.Symbol('x')
    y = syp.Symbol('y')
    xrel = syp.Symbol('xrel')
    yrel = syp.Symbol('yrel')
    rA = syp.Symbol('rA')
    rB = syp.Symbol('rB')

    circleA = syp.Eq(((x-xrel)**2) + ((y-yrel)**2), (rA**2))
    circleB = syp.Eq((x**2) + (y**2), (rB**2))

    solveArray = syp.solve([circleA, circleB], (x, y))
    
    return solveArray

def specAnglesCalc(valxrel, valyrel, valrA, valrB):
    
    x = syp.Symbol('x')
    y = syp.Symbol('y')
    xrel = syp.Symbol('xrel')
    yrel = syp.Symbol('yrel')
    rA = syp.Symbol('rA')
    rB = syp.Symbol('rB')

    circleA = syp.Eq(((x-xrel)**2) + ((y-yrel)**2), (rA**2))
    circleB = syp.Eq((x**2) + (y**2), (rB**2))

    solveArray = syp.solve([circleA, circleB], (x, y))

    subsDic = {xrel:valxrel, yrel:valyrel, rA:valrA, rB:valrB}

    solutions = []
    angles = []
    for i in range(0,len(solveArray)):
        pointx = syp.N(solveArray[i][0], subs=subsDic)
        pointy = syp.N(solveArray[i][1], subs=subsDic)

        print('Point x at:')
        print(pointx)

        print('Point y at:')
        print(pointy)

        solutions.append([pointx,pointy])
        angles.append(math.atan2(pointy, pointx))

    return angles

def sypOverlap():

    modeA = syp.Symbol('modeA')
    modeB = syp.Symbol('modeB')
    
    lb = syp.Symbol('lb')
    ub = syp.Symbol('ub')

    z1 = modeA - lb
    z2 = modeA - ub

    y1 = modeB - ub
    y2 = modeB - lb

    z = (z2-z1)/z2
    y = (y2-y1)/y2

    modeC = lb - ( (lb-ub)*(z/(z+y)) )

    modeC = syp.simplify(modeC)

    return modeC

    
