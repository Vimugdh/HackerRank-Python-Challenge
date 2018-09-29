'''
SUM AND PROD
'''
import numpy

def takeInput():
    n, m = map(int, input().strip().split())
    array = numpy.array([input().strip().split() for _ in range(n)], int)
    return array

def arrayOps(array):
    print(numpy.prod(numpy.sum(array, axis = 0)))
    
array = takeInput()
arrayOps(array)