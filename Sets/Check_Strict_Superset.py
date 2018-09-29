'''
CHECK STRICT SUPERSET
'''

setA = set(input().split())
N = int(input())
print(all(setA > set(input().split()) for _ in range(N)))

'''
'all' keyword returns True iff all the items passed to it are True
'>' operator checks Strict Super Set
'''