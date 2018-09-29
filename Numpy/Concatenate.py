'''
Concatenate
'''

import numpy

def takeInput():
    n, m, p = map(int, input().strip().split())
    return ([input().strip().split() for _unused_i in range(n)]), ([input().strip().split() for _unused_i in range(m)])

    
def arrayOperations(someList, someOtherList):
    array1 = numpy.array(someList, int)
    array2 = numpy.array(someOtherList, int)
    print(numpy.concatenate((array1, array2), axis = 0))


inputList, otherInputList = takeInput()
arrayOperations(inputList, otherInputList)

'''
It would beat the whole point of this exercise but this whole thing can be done without any 
concatination at all if simply take all the inputs in one extended list and convert it to an 
array like so:

def takeInput():
    n, m, p = map(int, input().strip().split())
    return ([input().strip().split() for _unused_i in range(n + m)]) #Extended range 

    
def arrayOperations(someList):
    array = numpy.array(someList, int)
    print(array)

inputList = takeInput()
arrayOperations(inputList)
'''