from collections import namedtuple

numberOfStudents = int(input())
Student = namedtuple('Student', input().split())
totalGrades = 0
for each_student in range(numberOfStudents):
    columns = input().split()
    each_student = Student(columns[0], columns[1], columns[2], columns[3])
    totalGrades += float(each_student.MARKS)
print(round(totalGrades/numberOfStudents, 2))

