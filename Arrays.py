'''
ARRAYS

'''

import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)
    
'''
#This is also a valid way to do it
def arrays(arr):
    arr.reverse()
    return numpy.array(arr, float)


#Also this
def arrays(arr):
    return numpy.array([num for num in reversed(arr)], float)

#The reason list comprehension was used above was because the reversed() function 
returns a list_reverseiterator object and the float() argument  must be a string
or a number. Thus using for loop to iterate over the iterator object.

#This won't work
def arrays(arr):
    return numpy.array(arr.reverse(), float)

#Also this won't work
def arrays(arr):
    return numpy.array([num for num in arr.reverse()], float)

#The reason is that arr.reverse() does an in-place reversal of the list and returns
None and 'NoneType' object is not iterable and passing it to the float() function
may work but it will just return an empty array like so:
array(nan)
'''

arr = input().strip().split(' ')
result = arrays(arr)
print(result)