import math


def Squares(a, b):
    number = int(math.sqrt(b))
    count = 0
    for each in range(number + 1):
        if a <= each ** 2 <= b:
            count += 1
    return count


def Squares2(a, b):
    startRange = a
    endRange = b
    a = int(round(math.sqrt(a)))
    b = int(round(math.sqrt(b)))
    if a == b:
        if startRange <= a ** 2 <= endRange:
            return 1
        else:
            return 0
    else:
        if a ** 2 < startRange:
            a += 1
        count = 0
        for number in range(a, b):
            count += 1
        if b ** 2 <= endRange:
            count += 1
        if (b + 1) ** 2 <= endRange:
            count += 1
        return count


testCases = int(input())
for test in range(testCases):
    start, end = map(int, input().split())
    print(Squares2(start, end))
