def gradingStudents(grades):
    for index in range(len(grades)):
        if grades[index] >= 38:
            if grades[index] == 38:
                grades[index] = 40
            else:
                count = 0
                next_mul_five = grades[index]
                while next_mul_five % 5 != 0:
                    count += 1
                    next_mul_five += 1
                if count < 3:
                    grades[index] = next_mul_five
    return grades


grades = []
numberOfStudents = int(input())

for i in range(numberOfStudents):
    grades.append(int(input()))

grades = gradingStudents(grades)
print(*grades, sep="\n")

