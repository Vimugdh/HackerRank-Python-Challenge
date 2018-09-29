'''
FIND THE RUNNER-UP SCORE!
'''

'''
sorted() sorts the list and ideally in case there are no duplicate elements, the second-largest
value shall bubble up to the [-2] place but to handle duplicate elements we use set(). set() 
removes the duplicate scores but then again, it doesn't support indexing so we have to use list()
to convert it to a list object in order to access the [-2] position through indexing. 
'''
def main(n, arr):
    print(sorted(list(set(arr)))[-2])

''' 
print(list(set(sorted(arr)))[-2])
Tried this and it failed because although the functions used are correct, the order is wrong. sorted(arr)
sorts the array but since a Python set is by definition an 'ordered set of unique elements', it messes up 
the order. Using the thus, corrected order.	
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    main(n, arr)
