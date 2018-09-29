'''
ZEROS AND ONES
'''

import numpy

'''
Here we take input in the form of a tuple because the numpy.zeros() and numpy.ones() functions
take input about the number of dimensions in the form of a tuple so we can directly pass this
to the functions
'''

def takeInput():
    return tuple(map(int, input().strip().split()))


def printZerosAndOnes(dimensionTuple):
    print(numpy.zeros((inputTuple), dtype = numpy.int))
    print(numpy.ones((inputTuple), dtype = numpy.int))

printZerosAndOnes(takeInput())