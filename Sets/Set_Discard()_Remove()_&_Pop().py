'''
SET.DISCARD(), .REMOVE() AND .POP()
'''

n = int(input())
s = set(map(int, input().split())) 
N = int(input())
for i in range(N):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))


'''
def takeInput():
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    cmdList = [input().split() for _ in range(N)]
    return s, cmdList

def setOps(s, cmdList):
    print(type(s))
    for item in cmdList:
        if item[0][0] == 'pop':
            s.pop()
        else:
            s = item[0].split()
            cmd = s[0]
            print(cmd)
            args = s[1:]
            #cmd = (item[0].split())[0]
            #print(cmd)
            #args = eval((item[0].split())[1])
            eval('s.{0}({1})'.format(cmd, args))
    print(sum(s))

s, cmdList = takeInput()
setOps(s, cmdList)

For some reason my code kept giving me TypeError: 'list' object cannot be interpreted as an integer
Any help about where I was going would be appreciated.
'''

n = int(input())
s = set(map(int, input().split())) 
N = int(input())
for i in range(N):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))