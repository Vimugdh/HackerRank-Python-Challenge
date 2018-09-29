'''
DIVISION 

'''
class Arithmetic:
    def squareList(self, a):
        return [num ** 2 for num in range(a)]
	
if __name__ == '__main__':
    a = int(input())
    for item in Arithmetic().squareList(a):
        print(item)