'''
MIN AND MAX
'''
import numpy

def takeInput():
    n, m = map(int, input().strip().split())
    array = numpy.array([input().strip().split() for _ in range(n)], int)
    return array


def arrayOps(array):
    print(numpy.max((numpy.min(array, axis = 1))))

    
array = takeInput()
arrayOps(array)
