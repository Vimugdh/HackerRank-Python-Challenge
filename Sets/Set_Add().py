'''
SET.ADD()
'''

def takeInput():
    N = int(input())
    stamps = [input() for _ in range(N)]
    return stamps


def countDistinctStamps(stamps):
    print(len(set(stamps)))


stamps = takeInput()
countDistinctStamps(stamps)