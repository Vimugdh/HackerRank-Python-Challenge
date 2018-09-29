'''
SYMMETRIC DIFFERENCE
'''
def takeInput():
    setA, setB = [set(input().split()) for _ in range(4)][1::2]
    return setA, setB

'''
This one starts by reading the 4th first lines:

[set(raw_input().split()) for _ in range(4)]
With the [...], those 4 inputs are stored in a list, which one is then explored by:

list[1::2]
This means [start:stop:step], like we start at list[1], stop at list[None] (this means we don't stop 
till the end of the list) and the step of the exploration is 2, so we got list[1], list[3], etc.

In our case, the list has length 4, so by list[1::2], we got members 2 and 4. Finally, with:

a,b = [set(raw_input().split()) for _ in range(4)][1::2]
the 2 lines are stored in variables a and b.

^^^
Found that in the Discussions section of the problem by some amazing dude 'newmocart'

Couldn't understand why the HackerRank tool kept returning 'EOF' on the input code that I had written
listA, listB = list(map(int, [(input().split()) for _ in range(4)]))

Also instead of using the '^' operator, one can also derive the set notation for symmetric difference
which would be (A - B).union((B - A)) for which the Python code would be like so:

def setOps(setA, setB):
    AdiffB = setA.difference(setB)
    BdiffA = setB.difference(setA)
    print('\n'.join(sorted(AdiffB.union(BdiffA), key = int)))

'''


def setOps(setA, setB):
    print('\n'.join(sorted(setA ^ setB, key = int)))

    
setA, setB = takeInput()
setOps(setA, setB)