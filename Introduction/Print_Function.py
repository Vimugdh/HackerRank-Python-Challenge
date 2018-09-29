'''
PRINT FUNCTION

'''

class Print:
    def main(self, n):
        for num in range(1, n + 1):
            print(num, end = '')

if __name__ == '__main__':
    n = int(input())
    Print().main(n)
    