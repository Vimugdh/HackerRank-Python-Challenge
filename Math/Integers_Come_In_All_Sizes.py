'''
INTEGERS COME IN ALL SIZES
'''

def takeInput():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return a, b, c, d
    
    
def printLargeInt(a, b, c, d):
    print(pow(a, b) + pow(c, d))

    
a, b, c, d = takeInput()
printLargeInt(a, b, c, d)