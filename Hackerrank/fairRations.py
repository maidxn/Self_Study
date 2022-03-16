def CheckEven(num):
    return 1 if num % 2 == 0 else 0


numberOfSubjects = int(input())
subjects = list(map(int, input().split()))

count = 0
for index in range(numberOfSubjects - 1):
    if not CheckEven(subjects[index]):
        subjects[index] += 1
        subjects[index + 1] += 1
        count += 1

if not CheckEven(subjects[numberOfSubjects - 1]):
    print("NO")
else:
    print(2 * count)

# I spent so much time on this problem. I know the problem is simple but I can't solve it
# quickly :<<<

