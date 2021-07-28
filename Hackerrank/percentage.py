student = {}
numberOfStudent = int(input())
for i in range(numberOfStudent):
    record = input().split()
    score = [float(i) for i in record[1:]]
    student[record[0]] = score
query_name = input()
totalScore = sum(student[query_name])
average = (totalScore / 3)
average = "{0:.2f}".format(average)
print(average)
