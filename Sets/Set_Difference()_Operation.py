'''
SET .DIFFERENCE() OPERATION
'''

def takeInput():
    setA, setB = [set(input().split()) for _ in range(4)][1::2]
    return setA, setB


def setOps(setA, setB):
    print(len(setA.difference(setB)))

    
setA, setB = takeInput()
setOps(setA, setB)