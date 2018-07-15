'''
NESTED LISTS
'''


def main(studentList):    
    marksList = [studentList[i][1] for i in range(len(studentList))]
    secondLowestMarks = list(sorted(set(marksList)))[1]
    studentsWithSecondLowestMarksList = [student[0] for student in studentList if student[1] == secondLowestMarks]
    sortedStudentsWithSecondLowestMarksList = sorted(studentsWithSecondLowestMarksList)
    for student in sortedStudentsWithSecondLowestMarksList:
        print(student)

    
if __name__ == '__main__':
    studentList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentList.append([name, score])
    main(studentList)
