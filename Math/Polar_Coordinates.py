'''
POLAR CO-ORDINATES
'''

import math
import cmath


def takeInput():
    return complex(input())


def printPolar(complexNum):
    print('{0:.3f}'.format(math.sqrt((complexNum.real ** 2) + (complexNum.imag ** 2))))
    print('{0:.3f}'.format(cmath.phase(complexNum)))

'''
Although the question asks for the result to be rounded off to 3 decimal places, it accepts
the answer even if you don't do so.
'''
    
complexNum = takeInput()
printPolar(complexNum)