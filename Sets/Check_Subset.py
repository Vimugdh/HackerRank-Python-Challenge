'''
CHECK SUBSET
'''

for _ in range(int(input())):
    nSetA = int(input())
    setA = set(input().split())
    nSetB = int(input())
    setB = set(input().split())
    if setA.issubset(setB): print(True)
    else: print(False)