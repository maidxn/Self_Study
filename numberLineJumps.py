def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:
        return False
    if (x1 - x2) % (v2 - v1) == 0:
        return True
    return False


posA, stepsA, posB, stepB = map(int, input().split())
if kangaroo(posA, stepsA, posB, stepB):
    print("YES")
else:
    print("NO")




