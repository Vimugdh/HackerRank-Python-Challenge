'''
ARITHMETIC OPERATORS 

'''
class Arithmetic:
    def operation(self, a, b):
        return (a + b), (a - b), (a * b)
	
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum, difference, product = Arithmetic().operation(a, b)
    print(sum)
    print(difference)
    print(product)