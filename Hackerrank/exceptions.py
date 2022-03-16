def CheckExceptions(a, b):
    try:
        ans = int(a) // int(b)
    except Exception as e:
        ans = "Error Code: " + str(e)
    return ans


testCases = int(input())
for each in range(testCases):
    first, second = input().split()
    print(CheckExceptions(first, second))

