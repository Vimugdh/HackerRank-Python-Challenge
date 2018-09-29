'''
FIND ANGLE MBC
'''

import math

def takeInput():
    AB = int(input())
    BC = int(input())
    return AB, BC


def printAngle(AB, BC):
    print(str(int(round(math.degrees(math.atan2(AB,BC))))) + '°')

'''
Using the property that the median of a right angled triangle divides the triangle
into two isosceles triangles.
'''
    
    
AB, BC = takeInput()
printAngle(AB, BC)