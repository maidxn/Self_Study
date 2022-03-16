def AppendAndDelete(stringS, stringT, n):
    count = 0
    pre = -1
    ans = "No"
    for index in range(len(stringS)):
        if index >= len(stringT):
            break
        if stringS[index] == stringT[index] and index - pre == 1:
            count += 1
            pre = index
    times = len(stringS) - count
    if stringS == stringT:
        ans = "Yes"
    elif count == 0:
        if len(stringS) + len(stringT) <= n:
            ans = "Yes"
    elif len(stringS) >= len(stringT) and n >= len(stringS) + len(stringT):
        ans = "Yes"
    elif times + (len(stringT) - count) == n:
        ans = "Yes"
    elif len(set(stringS)) == 1 and len(stringS) != 1:
        ans = "Yes"
    return ans


firstString = input()
secondString = input()
numberOfChanges = int(input())
print(AppendAndDelete(firstString, secondString, numberOfChanges))

