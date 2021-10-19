from collections import OrderedDict


orderedDict = OrderedDict()
numberOfItems = int(input())

for item in range(numberOfItems):
    new = input().split()
    price = int(new[-1])
    newItem = " ".join(new[:-1])
    if newItem in orderedDict.keys():
        orderedDict[newItem] += price
    else:
        orderedDict[newItem] = price
for key, value in orderedDict.items():
    print(key, value)


