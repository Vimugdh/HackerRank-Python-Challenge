'''
FIND A STRING(OVERLAPPING)
'''
def count_substring(string, sub_string):
    counter = 0
    lenSubString = len(sub_string)
    for _ in range(len(string)):
        if string[_ : _ + lenSubString] == sub_string:
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)