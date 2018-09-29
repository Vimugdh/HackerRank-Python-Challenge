'''
FLOOR, CEIL AND RINT
'''
import numpy

def takeInput():
    array = numpy.array(input().strip().split(), float)
    return array

def arrayOps(array):
    print(numpy.floor(array))
    print(numpy.ceil(array))
    print(numpy.rint(array))
    
array = takeInput()
numpy.set_printoptions(sign=' ') #Changing print options
arrayOps(array)