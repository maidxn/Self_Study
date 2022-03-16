def MigratoryBirds(arr):
    countTypes = [0] * 5
    for item in arr:
        countTypes[item - 1] += 1
    highestFre = countTypes[0]
    pos = 1
    for index in range(len(countTypes)):
        if countTypes[index] > highestFre:
            highestFre = countTypes[index]
            pos = index + 1
    return pos


size = int(input())
birds = [int(i) for i in input().split()]
print(MigratoryBirds(birds))

