def AngryProfessor(number, array):
    count = 0
    for item in array:
        if item <= 0:
            count += 1
        if count == number:
            print("NO")
            return
    print("YES")
    return


numberOfTestcase = int(input())
for testcase in range(numberOfTestcase):
    numberStudent, threshold = map(int, input().split())
    arrivalTimes = [int(i) for i in input().split()]
    AngryProfessor(threshold, arrivalTimes)
