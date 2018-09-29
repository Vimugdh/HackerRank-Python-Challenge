'''
PYTHON IF-ELSE

'''
#!/bin/python3
class Weirdness:
    def __init__(self, n):
        self.n = n
        
    def getWeirdness(self):
        if self.n % 2 != 0:
            print('Weird')
        else:
            if 2 <= self.n <= 5:
                print('Not Weird')
            elif 6 <= self.n <= 20:
                print('Weird')
            elif 20 < self.n:
                print('Not Weird')


N = int(input())
weirdness = Weirdness(N)
weirdness.getWeirdness()