'''
CAPITALIZE
'''
def solve(s):
    stringList = list(s)
    stringList[0] = stringList[0].upper()
    for index, character in enumerate(stringList):
        if character == ' ':
            stringList[index + 1] = stringList[index + 1].upper()
    return ''.join(stringList)