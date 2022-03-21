from datetime import datetime


testcases = int(input())
for testcase in range(testcases):
    # temp = input().split()
    # string = ' '.join(temp[:-1])
    # days, hours, mins = map(int, [temp[-1][1], temp[-1][2], temp[-1][3:]])
    # seconds_1 = days * converter[0] + hours * converter[1] + mins * converter[2]
    first = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    # temp2 = input().split()
    # string2 = ' '.join(temp2[:-1])
    # days, hours, mins = map(int, [temp2[-1][1], temp2[-1][2], temp2[-1][3:]])
    # seconds_2 = days * converter[0] + hours * converter[1] + mins * converter[2]
    second = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((first - second).total_seconds())))
# it has %z format ok? And I spent about 30 mins for this :)
# Stupid
# Where to find the ref: https://www.journaldev.com/23365/python-string-to-datetime-strptime



