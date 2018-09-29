'''
FINDING THE PERCENTAGE
'''


def main(query_name):
    sumOfMarks = 0
    countSubjects = 0
    for item in student_marks[query_name]:
        sumOfMarks += item
        countSubjects += 1
    print('{0:.2f}'.format(sumOfMarks / countSubjects)) #Printing correct to two decimal places

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    main(query_name)
