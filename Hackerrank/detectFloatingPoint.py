import re


condition = r"^[+-]?[0-9]*\.[0-9]+$"
testcases = int(input())
for testcase in range(testcases):
    print(bool(re.match(condition, input())))

# OR another way
for testcase in range(testcases):
    try:
        number = float(input())
        print(True)
    except ValueError:
        print(False)
