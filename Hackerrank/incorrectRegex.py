import re


numberOfTestcases = int(input())
for testcase in range(numberOfTestcases):
    pattern = input()
    ans = "True"
    try:
        re.compile(pattern)
    except re.error:
        ans = "False"
    print(ans)


