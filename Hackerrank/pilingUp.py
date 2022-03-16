def CheckAscending(array):
    for index in range(1, len(array)):
        if array[index - 1] > array[index]:
            return False
    return True


def CheckDescending(array):
    for index in range(1, len(array)):
        if array[index - 1] < array[index]:
            return False
    return True


def CheckGap(array):
    down = False
    for index in range(1, len(array)):
        if array[index - 1] < array[index] and down is False:
            down = True
        elif down:
            if array[index - 1] > array[index]:
                return False
    return True


testCases = int(input())
for testCase in range(testCases):
    size = int(input())
    arr = list(map(int, input().split()))
    asc = CheckAscending(arr)
    desc = CheckDescending(arr)
    if asc or desc:
        print("Yes")
    else:
        print("Yes" if CheckGap(arr) else "No")

# Oh, wao, I used Greedy :) great :>
# Another way is using deque, but I don't understand it clearly.
# It's simple is take the first and the last item to compare, like I did
# But it's more effective, it's a built-in data structure
