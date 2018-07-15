'''
SHAPE AND RESHAPE
'''
import numpy

def changeShape(someList):
    someArray = numpy.array(someList)
    return numpy.reshape(someArray, (3, 3))

'''
int is applied on each and every element in input list spit out by split() function and
map() function returns a map object which must be converted to a list.
However, passing the 'int' argument as dtype in numpy.array() function works as well
like so: 
inputList = input().strip().split() #Takes numbers input as string objects
someArray = numpy.array(inputList, int) #Converts them to int objects
The string objects inside someList will be converted to integer type implicitly.

'''

inputList = list(map(int, input().strip().split())) #Split by default takes ' ' (space literal) as input
print(changeShape(inputList))