'''
LINEAR ALGEBRA
'''
import numpy

def takeInput():
    N = int(input())
    array = numpy.array([input().strip().split() for _ in range(N)], float)
    return array


def arrayOps(array):
    print(numpy.linalg.det(array))
    

array = takeInput()
numpy.set_printoptions(legacy='1.13') #Change print options
arrayOps(array)
