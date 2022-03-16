dayOfPreviousMonths = 215


def CheckLeapYear(y):
    if y % 400 == 0:
        return 1
    if y % 4 == 0 and y % 100 != 0:
        return 1
    return 0


def CheckCalendar(y):
    global dayOfPreviousMonths
    if y == 1918:
        dayOfPreviousMonths += 15
    elif y < 1918:
        if y % 4 == 0:
            dayOfPreviousMonths += 29
        else:
            dayOfPreviousMonths += 28
    else:
        dayOfPreviousMonths += 28 + CheckLeapYear(y)


def DayOfProgrammer(y):
    global dayOfPreviousMonths
    CheckCalendar(y)
    septemberDay = 256 - dayOfPreviousMonths
    ans = str(septemberDay) + ".09." + str(y)
    return ans


year = int(input())
print(DayOfProgrammer(year))




