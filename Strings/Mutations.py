'''
MUTATIONS
'''
def mutate_string(string, position, character):
    stringList = list(string)
    stringList[position] = character
    newString = ''.join(stringList)
    return newString

'''
#This also works
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:] 
'''

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)