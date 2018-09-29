'''
sWAP cASE
'''
def swap_case(s):
    newS = ''
    for letter in s:
        if letter.isupper():
            newS += letter.lower()
        else:
            newS += letter.upper()
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)