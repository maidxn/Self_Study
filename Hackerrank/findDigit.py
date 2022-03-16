def FindDigits(integer):
    string = str(integer)
    count = 0
    for digit in string:
        if digit == '0':
            continue
        if integer % int(digit) == 0:
            count += 1
    return count


testcase = int(input())
for test in range(testcase):
    number = int(input())
    print(FindDigits(number))
