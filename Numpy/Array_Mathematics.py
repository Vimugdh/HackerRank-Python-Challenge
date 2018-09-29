'''
ARRAY MATHEMATICS
'''
import numpy

def takeInput():
    n, m = map(int, input().strip().split())
    array1 = numpy.array([input().strip().split() for _ in range(n)], int)
    array2 = numpy.array([input().strip().split() for _ in range(n)], int)
    return array1, array2

    
def arrayOperations(someList):
    print(numpy.add(array1, array2))
    print(numpy.subtract(array1, array2))
    print(numpy.multiply(array1, array2))
    print(array1 // array2)
    print(numpy.mod(array1, array2))
    print(numpy.power(array1, array2))


array1, array2 = takeInput()
arrayOperations(array1, array2)