'''
SET .UNION() OPERATION
'''

def takeInput():
    setA, setB = [set(input().split()) for _ in range(4)][1::2]
    return setA, setB


def setOps(setA, setB):
    print(len(setA.union(setB)))

    
setA, setB = takeInput()
setOps(setA, setB)