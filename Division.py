'''
DIVISION 

'''
class Arithmetic:
    def division(self, a, b):
        return (a // b), (a / b)
	
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    intDivision, floatDivision = Arithmetic().division(a, b)
    print(intDivision)
    print(floatDivision)