'''
NO IDEA
'''
'''
I find the use of the 'n' and 'm' variables is absolutely purposeless in this example
and leads to nothing but confusion. I have no idea why this problem is labeled as 
having 'Medium' difficulty though.
'''


def takeInput():    
    n, m = map(int, input().split())
    array = input().split(' ')
    setA = set(input().split(' '))
    setB = set(input().split(' '))
    return array, setA, setB


def getHappiness(array, setA, setB):
    happiness = 0
    for num in array:
        if num in setA: happiness += 1
        elif num in setB: happiness -= 1
    return happiness


array, setA, setB = takeInput()
happiness = getHappiness(array, setA, setB)
print(happiness)
