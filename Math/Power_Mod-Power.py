'''
POWER MOD-POWER
'''

def takeInput():
    a = int(input())
    b = int(input())
    m = int(input())
    return a, b, m
    
    
def printPowMod(a, b, m):
    print(pow(a, b), pow(a, b, m), sep = '\n')

    
a, b, m = takeInput()
printPowMod(a, b, m)