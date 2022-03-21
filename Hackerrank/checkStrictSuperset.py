setA = set(map(int, input().split()))
numberOfOthers = int(input())
flag = True
for each in range(numberOfOthers):
    another = set(map(int, input().split()))
    if not setA.issuperset(another):
        flag = False
        break
print(flag)
