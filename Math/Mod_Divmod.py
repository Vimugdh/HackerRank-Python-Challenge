'''
MOD DIVMOD
'''

def takeInput():
    a = int(input())
    b = int(input())
    return a, b
    
    
def printDivMod(a, b):
    getDivMod = divmod(a, b)
    print(getDivMod[0], getDivMod[1], getDivMod, sep = '\n')

    
a, b = takeInput()
printDivMod(a, b)