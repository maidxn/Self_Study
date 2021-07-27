numberOfStudent = int(input())
names = []
grades = []

for i in range(numberOfStudent):
    names.append(input())
    grades.append(float(input()))

pos = []
lowest, almostLowest = 100, 100

for grade in grades:
    if grade < lowest:
        almostLowest = lowest
        lowest = grade
    elif grade != lowest and grade < almostLowest:
        almostLowest = grade

for index in range(len(grades)):
    if grades[index] == almostLowest:
        pos.append(index)

ans = []
for item in pos:
    ans.append(names[item])

ans.sort()
print(*ans, sep = "\n")




