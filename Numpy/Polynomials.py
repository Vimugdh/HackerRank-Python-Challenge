'''
POLYNOMIALS
'''
import numpy

def takeInput():
    polynomial = list(map(float, input().strip().split()))
    positionX = int(input())
    return polynomial, positionX
    

def arrayOps(polynomial, positionX):
    print(numpy.polyval(polynomial, positionX))


polynomial, positionX = takeInput()
arrayOps(polynomial, positionX)
