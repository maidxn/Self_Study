searchValue = int(input())
arraySize = int(input())
array = [int(i) for i in input().split()]

pos = 0
for item in array:
    if item == searchValue:
        print(pos)
        break
    pos += 1
