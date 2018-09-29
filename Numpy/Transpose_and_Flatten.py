'''
TRANSPOSE AND FLATTEN
'''
import numpy

'''
The for loop in list comprehension just runs n (number of rows) times because we take the
input for each row in separate lines (counting for the number of rows or loops iterations)
instead of all the elements in one single line in which case the number of times the loop
ran should've been n*m 
'''

def takeInput():
    n, m = map(int, input().strip().split())
    return ([input().strip().split() for _unused_i in range(n)])

    
def arrayOperations(someList):
    array = numpy.array(someList, int)
    print(array.transpose())
    print(array.flatten())

'''
A list can be flattened using a list comprehension like so:
someList = [[1,2],[3,4]]
flatList =  [num for i in range(len(someList)) for num in someList[i]]
'''

inputList = takeInput()
arrayOperations(inputList)