'''
EYE AND IDENTITY
'''
'''
The solution checking in this problem is a bit weird and expects extra spaces in the printing so
I changed the print options for numpy using a small line of code I found in the Discussions section
of the same problem by some amazing guy 'nprajilesh' 
'''
import numpy

n, m = map(int, input().strip().split())
numpy.set_printoptions(sign=' ') #Changing print options
print(numpy.eye(n, m, k = 0))
