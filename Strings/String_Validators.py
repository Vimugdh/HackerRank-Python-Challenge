'''
STRING VALIDATORS
'''
def main(s):
    alphanum = alpha = digit = lower = upper = False
    for character in s:
        if character.isalnum(): alphanum = True
        if character.isalpha(): alpha = True
        if character.isdigit(): digit = True
        if character.islower(): lower = True
        if character.isupper(): upper = True
    print(alphanum, alpha, digit, lower, upper, sep = '\n')

if __name__ == '__main__':
    s = input()
    main(s)