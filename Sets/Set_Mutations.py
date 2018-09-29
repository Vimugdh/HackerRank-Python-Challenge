'''
SET MUTATIONS
'''

n = int(input())
setA = set(input().split())
for _ in range(int(input())):
    eval('setA.{0}({1})'.format((input().split())[0], set(input().split())))
print(sum(map(int, setA)))
