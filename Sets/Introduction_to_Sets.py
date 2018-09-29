'''
INTRODUCTION TO SETS
'''
def average(array):
    distinctItems = set(array)
    return sum(distinctItems) / len(distinctItems)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)