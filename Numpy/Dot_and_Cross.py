'''
DOT AND CROSS
'''
import numpy

def takeInput():
    N = int(input())
    A = numpy.array([input().strip().split() for _ in range(N)], int)
    B = numpy.array([input().strip().split() for _ in range(N)], int)
    return A, B


def arrayOps(A, B):
    print(numpy.dot(A, B))

    
A, B = takeInput()
arrayOps(A, B)
