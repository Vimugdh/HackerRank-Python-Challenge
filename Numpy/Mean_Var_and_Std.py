'''
MEAN, VAR AND STD
'''
import numpy

def takeInput():
    n, m = map(int, input().strip().split())
    array = numpy.array([input().strip().split() for _ in range(n)], float)
    return array


def arrayOps(array):
    print(numpy.mean(array, axis = 1))
    print(numpy.var(array, axis = 0))
    print(numpy.std(array))


array = takeInput()
numpy.set_printoptions(legacy='1.13') #Changing print options
arrayOps(array)
