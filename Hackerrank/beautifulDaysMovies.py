def ReverseNum(num):
    string = str(num)
    string = string[::-1]
    return int(string)


def CheckDays(num, div):
    res = 1 if abs(num - ReverseNum(num)) % div == 0 else 0
    return res


start, end, divisor = map(int, input().split())

days = 0
for each in range(start, end + 1):
    days += CheckDays(each, divisor)

print(days)
