def UtopianTree(n):
    if n == 0:
        return 1
    height = 1
    for item in range(1, n + 1):
        if item % 2 == 0:
            height += 1
        else:
            height *= 2
    return height


testCase = int(input())
for test in range(testCase):
    cycles = int(input())
    print(UtopianTree(cycles))
