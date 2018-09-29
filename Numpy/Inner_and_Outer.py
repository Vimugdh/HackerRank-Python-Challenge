'''
INNER AND OUTER
'''
import numpy

def takeInput():
    A = numpy.array(input().strip().split(), int)
    B = numpy.array(input().strip().split(), int)
    return A, B


def arrayOps(A, B):
    print(numpy.inner(A, B))
    print(numpy.outer(A, B))

    
A, B = takeInput()
arrayOps(A, B)
