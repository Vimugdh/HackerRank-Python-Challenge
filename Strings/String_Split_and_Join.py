'''
STRING SPLIT AND JOIN
'''
def split_and_join(line):
    return "-".join(line.split())

'''
#This also works
def split_and_join(line):
    return line.replace(" ", "-")
'''

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)